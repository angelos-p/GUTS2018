import sys
commands = {
    "/weather": "weather",
    "/light": "light",
    "/music": "music",
    "/annoying": "annoying"
}
weather = False
light = False
music = False
annoying = False

def main():
    while True:
        command = str(raw_input("Hi Please tell me what to do: "))
        if command == "" or command[0] != "/":
            print "Please enter a valid command!"
        else:
            if command in commands.keys():
                print commands[command]
            elif command == "/quit":
                print "Goodbye!"
                break
            else:
                print "Command not found!"
