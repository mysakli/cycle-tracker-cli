from sqlalchemy import create_engine, select, func, MetaData, Table
from sqlalchemy import Column, Integer, Date, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound 
import click
from datetime import  datetime, timedelta, date
# import datetime

db = create_engine("sqlite:///periods.sqlite")

Base = declarative_base()


def connect():
  Base.metadata.create_all(db)
  Session = sessionmaker(bind=db)
  return Session()



class Period(Base):
  __tablename__ = 'periods'

  id = Column(Integer, primary_key=True)
  start_date = Column(Date)
  end_date = Column(Date)
  duration = Column(Integer)
  cycle_length = Column(Integer)
  avg_cycle_length = Column(Float)

  def __repr__(self):
    return f'Cycle: {self.id} started on {self.start_date}'


@click.group()
def cycle():
  pass

@cycle.command()
@click.option('--start', prompt='First day of period (DD-MM-YYYY)')
@click.option('--end', prompt='Last day of period (DD-MM-YYYY)')
def add(start, end):
  session = connect()
  
  f_start = datetime.strptime(start, '%d-%m-%Y').date()
  f_end = datetime.strptime(end, '%d-%m-%Y').date()
  
  period = Period(start_date = f_start, end_date = f_end)
  duration = period.end_date - period.start_date
  period.duration = duration.days

  try:
    last_id = session.query(func.max(Period.id)).scalar()
    previous_period = session.query(Period).filter_by(id = last_id).one()
    cycle_length = period.start_date - previous_period.end_date
    period.cycle_length = cycle_length.days
  except NoResultFound:
    period.cycle_length = None
  
  
  session.add(period)
  session.commit()

  period.avg_cycle_length = session.query(func.avg(Period.cycle_length)).scalar()

  session.add(period)
  session.commit()
  
  if period.avg_cycle_length == None:
    click.echo(f'Cycle added! Average cycle length couldn\'t be calculated yet.')
  else:
    click.echo(f'Cycle added! Average cycle length is {int(period.avg_cycle_length)} days.')

@cycle.command()
@click.option('--all', prompt='Do you want to list all entries?', is_flag=True, help='Lists given number of entries')
def overview(all):
  session = connect() 
  queryset = session.query(Period).all()
  entries_count = session.query((func.count(Period.id))).scalar()

  if all == False:
    queried_entries = int(input(f'How many recent entries do you want to see (max. {entries_count})? '))
    
    queryset = session.query(Period).filter(Period.id > entries_count - queried_entries)
  
  for period in queryset:
    click.echo(f'{period.start_date} | {period.end_date} | {period.duration} days| {period.cycle_length} | {period.avg_cycle_length}')
   
     
 

@cycle.command()
@click.option('--period_id', prompt='Period ID to be deleted', help='Delete entry by period ID')
def delete(period_id):
  session = connect()
  period = session.query(Period).filter_by(id = period_id).one()
  session.delete(period)
  session.commit()

  click.echo(f'Period with ID {period_id} deleted.')

@cycle.command()
def next():
  session = connect()

  avg_cycle_length = session.query((func.avg(Period.cycle_length))).scalar()
  today = date.today()

  next_period_start = today + timedelta(days = avg_cycle_length)
  
  print(f'Next period is expected to start on {next_period_start}. Average cycle length is {avg_cycle_length} days.')

  


if __name__ == "__main__":
    cycle()