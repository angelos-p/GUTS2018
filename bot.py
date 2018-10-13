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
    previous = "/weather"

    while True:
        command = str(raw_input("Hi Please tell me what to do: "))
        if command == "" or command[0] != "/":
            print "Please enter a valid command!"
        else:
            if command == "/all":
                choice = random.choice(commands.keys())
                while choice == previous:
                    previous = choice
                    choice = random.choice(commands.keys())
                previous = choice
                commands[choice]()
            elif command in commands.keys():
                previous = command
                commands[command]()
            elif command == "/quit":
                print "Goodbye!"
                break
            else:
                print "Command not found!"

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    main()
