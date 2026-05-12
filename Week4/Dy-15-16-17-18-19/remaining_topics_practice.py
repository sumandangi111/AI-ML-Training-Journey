'''
Context managers 
Logging 
Environment configuration (.env) 
API handling basics 
Intro to async programming'''

#-----------------Context managers--------------------
# context managers are objects that manage the allocation and release of resources
# When you work with things like files or database connections, you have to remember to "open" them and then "close" them when you're done. If you forget to close them, your program might waste memory or crash.
# A context manager does this work for you automatically using the with keyword.

# with open("sample.txt","r") as f:
#     print(f.read())

#-------------------Logging-----------------------------
#  You use logging because it provides a permanent, searchable history of your program’s behavior that you can customize without changing your code.
# Logging in Python is handled by the built-in logging module, which allows you to track events, diagnose problems, and record program execution without using print() statements.
# Loggers, Handlers, Formatters, Filters
'''
Level     Numeric Value     Use Case
DEBUG        10             Detailed diagnostic information.
INFO         20             Confirmation that things are working as expected.
WARNING      30             Something unexpected happened (default level).
ERROR        40             A serious problem; the software couldn't perform a function.
CRITICAL     50             A fatal error; the program may be unable to continue
'''

import logging
# 1. Setup: Where to save and what level to track
logging.basicConfig(filename='my_diary.log', level=logging.INFO)
# 2. Writing notes
logging.info("The program started successfully.")
logging.warning("Memory is getting a bit full.")
logging.error("Could not find the user's profile!")

#--------------------------------- (.env) ----------------
# .env - a configuration file for storing sensitive variables or virtual environment directory
#.env is a plain text file used to store project-specific settings and 'secret' like API keys,database credentials
'''
inside .env file :-
API_KEY=your_secret_key_here
DEBUG=True
DB_URL=
'''

'''
to load this variables in our code use dotenv library
to install library: pip install python-dotenv

import os
from dotenv import load_dotenv
load_dotenv() to loads variables from .env into the environment
api_key=os.getenv("API_KEY")
'''

# .env virtual environment :- it isolates your project's dependencies (libraries like Django, pandas) so they don't interfere with other projects on your computer
'''to create :-
windows: python -m venv .env
'''

'''to activate:-
.env\Scripts\activate
'''

