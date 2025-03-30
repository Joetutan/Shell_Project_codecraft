

import sys
import shutil
import subprocess
from pathlib import Path


def main():
    # Uncomment this block to pass the first stage
    builtin = ["echo", "exit", "type", "pwd"]
    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        user_input = input()
        args_ = user_input.split()
        match args_:
            case ["echo", *args]:
                print(*args)
            case ["cd", *args]:
                path = args
                if path.is_dir():
                     Path.chdir(path)
                else:
                     print(f"cd: {path}}: No such file or directory")
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
                         
                    print(F"Program was passed {len(args_)} args (including program name).")
                    print(f"Arg #0 (program name): {ex_path}")
                    print(f"Arg #1: {ex_name_}")
                    print(f"Program Signature: {get_signature(path)}")
            case _:
                print(f"{user_input}: command not found")

def get_signature(path):
            result = subprocess.run([path],capture_output=True, text=True)
            stdout_lines = result.stdout.splitlines()

            for line in stdout_lines:
                    if "Program Signature:" in line:
                        signature = line.split("Program Signature:")[1].strip()
                        break
            return signature
if __name__ == "__main__":
    main()













