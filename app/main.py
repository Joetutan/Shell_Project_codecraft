

import sys
import shutil
def main():
    # Uncomment this block to pass the first stage
    builtin = ["echo", "exit", "type"]
    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        user_input = input()
        match user_input.split():
            case ["echo", *args]:
                print(*args)
            case ["exit", "0"]:
                sys.exit(0)
            case ["type", arg]:
                if arg in builtin:
                    print(f"{arg} is a shell builtin")
                elif path := shutil.which(arg):
                    print(f"{arg} is {path}")
                else:
                    print(f"{arg}: not found")
            case _:
                print(f"{user_input}: command not found")
if __name__ == "__main__":
    main()













"""import sys
import shutil

def main():
 
     while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        
        if command == "exit 0":
            break

        if command.startswith("echo "):
            get_echo(command)
        elif command.startswith("type "):
            get_type(command)
        else:  
            get_path(command)
        #
        
       
def get_type(command):
        type_list = ["echo","exit", "type"]
        if command[5:] in type_list:
                print(f"{command[5:]} is a shell builtin")
        else:
             print(f"{command[5:]}: not found")

def get_echo(command):
        print (command[5:])

def get_path(command): 
    command_path = shutil.which(command[5:])
    if command_path:
              print(command_path)
    else:
              print(f"{command[5:]}: not found")
    


if __name__ == "__main__":
    main()"""
