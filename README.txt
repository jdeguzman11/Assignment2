ICS 32 – Assignment 2: Journal
Author: Justin DeGuzman

Description
-----------
This program is a command-line journal application. Users can create or open a journal
file, store profile information (username, password, bio), write journal posts, delete
posts, and print saved data. Journal data is stored in a DSU file using JSON through the
provided Profile module.

The program supports two modes:
- Friendly mode with guided prompts
- Admin mode with strict command-based input

Features
--------
- Create and open DSU journal files (supports paths with spaces)
- Save and load profile data
- Add, delete, and view journal posts
- Print profile information and posts
- Error handling for invalid input

Main Commands (Admin Mode)
--------------------------
C <directory> -n <name>     Create a journal
O <file>                   Open a journal
E [options]                Edit profile or posts
P [options]                Print profile or posts
L / D / R                  File system commands
Q                          Quit

Files
-----
a2.py                 Program entry point
ui.py                 User interface and command processing
command_processor.py  File system commands
Profile.py            Provided profile module
README.txt            This file

Usage
-----
Run with:
    python3 a2.py

Type "admin" at startup to use admin mode.
