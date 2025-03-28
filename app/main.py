import sys


def main():
     #Uncomment this block to pass the first stage
     

     # Wait for user input
     #input()
     #read the command 
     while True:
        sys.stdout.write("$ ")
        command = input()
        type_list = ["echo","exit", "type"]
       
        if command[5:] in type_list:
            print(f"{command[5:]} is a shell builtin")
        elif command == "exit 0":
            break
        elif command.startswith("echo "):
            print (command[5:])
        else:
            print(f"{command[5:]}: not found")
        



if __name__ == "__main__":
    main()
