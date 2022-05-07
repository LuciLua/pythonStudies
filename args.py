import requests
import argparse

parser = argparse.ArgumentParser(description="Passando argumentos...")

def printarHello():
    print("Hello, world!")
    
parser.add_argument('-d', '--debug', help="[OPTIONAL] debug")

args = parser.parse_args()

if args.debug:
    print("hello, world!" + args.debug)