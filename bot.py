import sys
import random

from weather import weatherMethod
from polly_talk import make_polly_talk

commands = {
    "/weather": weatherMethod,
    "/polly": make_polly_talk
}

def main():
    previous = "/weather"

    while True:
        command = str(raw_input("Please tell me what to do: "))
        sentence=""
        if command == "" or command[0] != "/":
            print "Please enter a valid command!"
        else:
            if command == "/all":
                choice = random.choice(commands.keys())
                while choice == previous:
                    previous = choice
                    choice = random.choice(commands.keys())
                previous = choice
                if choice == "/polly":
                    sentence = str(raw_input("Add a sentence: "))
                commands[choice](sentence)
            elif command in commands.keys():
                previous = command
                if command == "/polly":
                    sentence = str(raw_input("Add a sentence: "))
                commands[command](sentence)
            elif command == "/quit":
                print "Goodbye!"
                break
            else:
                print "Command not found!"

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    main()
