# import requests
import argparse
from datetime import datetime
from requests import options
# import json
import rich
import os

# Args
parser = argparse.ArgumentParser(
    description="Welcome to lissynt",
    prog='tool',
    formatter_class=lambda prog: argparse.HelpFormatter(
        prog,
        max_help_position=100, 
      )
  )

args = [
        ('-p', '--printh', 'print hello', {}),
        ('-t', '--test', '[OPTIONAL] test argsArePassed', {}),
        ('-d', '--date', '[OPTIONAL] show what time is it', {},)
        ]

for args1, args2, description, options in args:  
     parser.add_argument(args1, args2, help=description, nargs="?", const="-", **options)

args = parser.parse_args()

# Collors
class Colors:
    greenHacker = "#31D441"
    blueFace = "#2F46CE"
    blueBaby = "#5696C1"
    pinkFosco = "#C059D1"
    red = "#FF241D"

# Errors
def errors(type, msg):
    class Types:
        warning = "#FAB600"
        erro = "#FA3901"
        hardError = "#FF0701"

    if type == 1: 
        levelError = Types.warning
    if type == 2: 
        levelError = Types.erro
    if type == 3: 
        levelError = Types.hardError
    
    rich.print("\n[{0} ]- Erro: {1}\n".format(levelError, msg))

# Options: Functions
def printarHello(msg):
    rich.print("\nHello,[{0} underline] {1}![/] You are very welcome to my code, I hope that you find what need as I have been writing this code specially for devs as well as you\n".format(Colors.greenHacker, msg))
    
    rich.print("Visit my portfólio: [#356DFA underline]https://luci-lua.tk/ \n")
    
def helper():
    rich.print("[{0}]\n _          _                 ".format(Colors.greenHacker))
    rich.print("[{0}]| |__   ___| |_ __   ___ _ __".format(Colors.greenHacker))
    rich.print("[{0}]| '_ \ / _ \ | '_ \ / _ \ '__|".format(Colors.greenHacker))
    rich.print("[{0}]| | | |  __/ | |_) |  __/ |   ".format(Colors.greenHacker))
    rich.print("[{0}]|_| |_|\___|_| .__/ \___|_|   ".format(Colors.greenHacker))
    rich.print("[{0}]             |_|              \n".format(Colors.greenHacker))
    
    rich.print("[{0}] You can try pass -i for install all packages too\n".format(Colors.blueBaby))
    
def argsArePassed(argPassed, test):
    
    if argPassed == True:
        color = Colors.blueBaby
    else:
        color = Colors.red
    
    rich.print("[{0}]_____________________________".format(Colors.pinkFosco))
    rich.print("[{0}]Args passed: [{1}]{2} ".format(Colors.pinkFosco, color, argPassed))
    rich.print("[{0}]_____________________________".format(Colors.pinkFosco))
    rich.print("[{0}]Args passed: [{1}]{2} ".format(Colors.pinkFosco, color, test))
   
def showTheDate():

    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    
    hour = datetime.now().hour
    min = datetime.now().minute
    sec = datetime.now().second
    
    today = "{0}/{1}/{2}".format(day, month, year)
    
    time = "{0}:{1}:{2}".format(hour, min, sec)
    
    dateFormat = "\nDate of today: {0} \nWhat time is it: {1}\n".format(today, time)
    
    rich.print("[{0}] {1}".format(Colors.blueBaby, dateFormat))

# Conditional structures
# Case cli have some sufix 
if args.printh or args.test or args.date:
    # printh conditionals
    if args.printh == "-":
        errors(1, "not arg")
    elif args.printh:
        printarHello(args.printh)
    # Test conditionals
    if args.test == '-': 
        argsArePassed(False, False)
    elif args.test:
        argsArePassed(True, args.test)
    # Date conditionals
    if args.date == '-': 
        showTheDate()
    elif args.date:
        errors(2, "Please, don't put nothing in this area. Just leave it empty" )
# Case cli not have sufixes
else:
    errors(1, "None option passed" )
    helper()
    os.system("cli -h")
    print("\n")