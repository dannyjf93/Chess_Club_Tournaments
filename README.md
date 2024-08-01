# Chess_Club_Tournaments
This is a set of applications one of which is used to manage chess clubs and their corresponding players and the other to create/track tournaments for those players.

### Features Included
**Club management** Enable club managers to create new clubs, add new players to clubs, and edit existing players within a given club. 

**Player Registration:** Enable players to register by providing their name, email, birthdate, and National Chess ID.

**Tournament Creation/Management:** Tournament organizers are able to create new tournaments, register players from all available clubs, set the number of rounds per tournament, and record matches/player rankings.

**Match Pairing:** Dynamically pair players in matches based on points gained in each successive match. 

**Result Recording:** Results are recorded for each match within a tournament showing the match pairings, round results, points per player, and player rankings.

**Report Generation:** Reports available to display player information and tournament results.

# Running the application from the terminal
### Mac:
    Download files from this repository or create a clone using the code below
    $ git clone https://github.com/dannyjf93/Chess_Club_Tournaments.git
    
    Navigate to the directory containing the repository
    $ cd Chess_Club_Tournaments

    Create and activate a virtual environment
    $ python -m venv env

    Install required packages
    $ pip install -r requirements.txt
    
    Run the application
    $ python main.py


### Windows Powershell
    Download files from this repository or create a clone using the code below
    $ git clone https://github.com/dannyjf93/Chess_Club_Tournaments.git
    
    Navigate to the directory containing the repository
    $ cd Chess_Club_Tournaments

    Create and activate a virtual environment
    $ python -m venv env

    Install required packages
    $ pip install -r requirements.txt
    
    Run the application
    $ python main.py

# Generating a flake8 report
### Mac:
    Create virtual environment
    $ python -m venv env

    Generate report
    $ flake8 --format=html --htmldir=flake8_report

    
### Windows Powershell
    Create virtual environment
    $ python -m venv env
    
    Generate report
    $ flake8 --format=html --htmldir=flake8_report

### Future improvements
    1. Make tournament attributes editable except for number of rounds
    2. Add functionality to "retire" players from a chess club so that they can no longer be registered for tournaments

### Important notes
    This application was created using Python version 3.12.4 - all requirements for this application are satisfied by libraries already included in Python 3.12.4
    Scripting and extensive debugging was completed using PyCharm Community Edition 2024.1.1
    