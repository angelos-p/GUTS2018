import sys
import random

from weather import weatherMethod
from light import lightMethod
from music import musicMethod
from annoying import annoyingMethod

commands = {
    "/weather": weatherMethod,
    "/light": lightMethod,
    "/music": musicMethod,
    "/annoying": annoyingMethod
}

def main():
    while True:
        command = str(raw_input("Hi Please tell me what to do: "))
        if command == "" or command[0] != "/":
            print "Please enter a valid command!"
            continue
        else:
            if command == "/all":
                random.choice(commands.values())()
            elif command in commands.keys():
                commands[command]()
                continue
            elif command == "/quit":
                print "Goodbye!"
                break
            else:
                print "Command not found!"

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    main()
