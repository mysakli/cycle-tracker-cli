# cycle-tracker-cli
CLI app for tracking menstrual cycles.

This is an app written in Python that uses the CLICK library for command-line interface, and SQLAlchemy library for data storage. Pipenv is used as the package manager.

## Requirements

To run this app, you need the following requirements:

- Python 3.6 or higher
- Pipenv package manager

### Installation
To install this app, follow these steps:

1. Clone/fork the repository from GitHub
2. Navigate to the project directory and install the dependencies using Pipenv:

        pipenv install

3. Activate the virtual environment:

        pipenv shell

## Usage

To run the app, use the cli.py file in the root directory. You can use the following commands:


        python cycle-tracker.py <command> [options]


### Here is a list of commands available:

**`add`** | Adds a new period

**`overview`** | Displays all or given number of entries (starting with the most recent one)

**`delete`** | Deletes a period entry

**`next`** | Calculates the expected date of the next period 

Example:

    python cycle-tracker.py overview
    
**Important!** 

 If you intend to use the database for personal tracking, make sure to delete the example data first.

## License
This app is licensed under the MIT License. See the LICENSE file for more information.
