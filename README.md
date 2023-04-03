# cycle-tracker-cli
CLI app for tracking menstrual cycles.

This is an app written in Python that uses the CLICK library for command-line interface, and SQLAlchemy library for data storage. Pipenv is used as the package manager.

## Requirements

To run this app, you need the following requirements:

Python 3.6 or higher
Pipenv package manager
Installation
To install this app, follow these steps:

Clone/fork the repository from GitHub:
git
Navigate to the project directory and install the dependencies using Pipenv:

    pipenv install

Activate the virtual environment:

    pipenv shell

## Usage

To run the app, use the cli.py file in the root directory. You can use the following commands:


        python cycle-tracker.py <command> [options]
Here is a list of commands available:

- `new` :  Adds a new period
- `overview` : Displays selected data // tbd
- `delete` : Deletes a period entry
- `next` : Shows the average cycle length and calculates the expected date of the next 

Each command has its own options and parameters. You can see the details of each command using the --help option:


    python cli.py <command> --help

## License
This app is licensed under the MIT License. See the LICENSE file for more information.
