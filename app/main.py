import sys


def main():
     #Uncomment this block to pass the first stage
     

     # Wait for user input
     #input()
     #read the command 
     while True:
        sys.stdout.write("$ ")
        command = input()
        if command == "exit 0":
            break
        elif command.startswith("echo "):
            print (command[5:])
        else:
            print(f"{command}: command not found")
        



if __name__ == "__main__":
    main()
