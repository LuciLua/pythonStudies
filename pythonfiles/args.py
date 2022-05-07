# import requests
import argparse
from typing import Optional
# import json
import rich
import os

os.system('clear')

# Args
parser = argparse.ArgumentParser(description="Welcome to lissynt")

# Collors
class Colors:
    greenHacker = "#31D441"
    blueFace = "#2F46CE"
    blueBaby = "#5696C1"
    pinkFosco = "#C059D1"
    red = "#FF241D"

def printarHello(msg):
    rich.print("Hello,[{0} underline] {1}![/] You are very welcome to my code, I hope that you find what need as I have been writing this code specially for devs as well as you".format(Colors.greenHacker, msg))
    
    rich.print("Visit my portfólio: [#356DFA underline]https://luci-lua.tk/")
    
def helper():
    rich.print("[{0}] _          _                 ".format(Colors.greenHacker))
    rich.print("[{0}]| |__   ___| |_ __   ___ _ __".format(Colors.greenHacker))
    rich.print("[{0}]| '_ \ / _ \ | '_ \ / _ \ '__|".format(Colors.greenHacker))
    rich.print("[{0}]| | | |  __/ | |_) |  __/ |   ".format(Colors.greenHacker))
    rich.print("[{0}]|_| |_|\___|_| .__/ \___|_|   ".format(Colors.greenHacker))
    rich.print("[{0}]             |_|              ".format(Colors.greenHacker))
    
    rich.print("[{0}] You can try pass -h or --help as a param for see the commands avaliable".format(Colors.blueBaby))
    
def draw(argPassed, test):
    
    if argPassed == True:
        color = Colors.blueBaby
    else:
        color = Colors.red
    
    rich.print("[{0}]_____________________________".format(Colors.pinkFosco))
    rich.print("[{0}]Args passed: [{1}]{2} ".format(Colors.pinkFosco, color, argPassed))
    rich.print("[{0}]_____________________________".format(Colors.pinkFosco))
    rich.print("[{0}]Args passed: [{1}]{2} ".format(Colors.pinkFosco, color, test))
   
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
    
    rich.print("[{0}]- Erro: {1}".format(levelError, msg))


parser.add_argument('-d', '--debug', help="[OPTIONAL] debug")
parser.add_argument('-t', '--test', help="[OPTIONAL] test draw", nargs="?", const='nothing')

args = parser.parse_args()

if args.debug or args.test:
    if args.debug:
        printarHello(args.debug)
    # Verify if receive a arg
    elif args.test == 'nothing': 
        draw(False, False)
    elif args.test:
        draw(True, args.test)
        # if not receive a arg
else:
    errors(1, "None arg passed" )
    helper()