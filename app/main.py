

import sys
import shutil
import subprocess
import random

def main():
    # Uncomment this block to pass the first stage
    builtin = ["echo", "exit", "type"]
    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        user_input = input()
        args_ = user_input.split()
        match args_:
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
            case [ex_path,ex_name_]:
                if path := shutil.which(ex_path):

                    result = subprocess.run([path],capture_output=True, text=True)
                    stdout_lines = result.stdout.splitlines()

                    for line in stdout_lines:
                         if "Program Signature:" in line:
                                signature = line.split("Program Signature:")[1].strip()
                                break
                         
                    print(F"Program was passed {len(args_)} args (including program name).")
                    print(f"Arg #0 (program name): {ex_path}")
                    print(f"Arg #1: {ex_name_}")
                    print(f"Program Signature: {signature}")
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
