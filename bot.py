import sys
import random

from weather import weatherMethod
from polly_talk import make_polly_talk

commands = {
    "/weather": weatherMethod,
    "/polly": make_polly_talk
}

def main(command,sentence):
    previous = ""
    
    if command == "/all":
        choice = random.choice(commands.keys())
        while choice == previous:
            previous = choice
            choice = random.choice(commands.keys())
        previous = choice
        commands[choice](sentence)
    elif command in commands.keys():
        previous = command
        commands[command](sentence)
    else:
        print "Command not found!"

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    main()
