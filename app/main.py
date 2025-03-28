import sys


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
              print(f"{command}: command not found")

       
def get_type(command):
        type_list = ["echo","exit", "type"]
        if command[5:] in type_list:
                print(f"{command[5:]} is a shell builtin")
        else:
             print(f"{command[5:]}: not found")

def get_echo(command):
        print (command[5:])
    


if __name__ == "__main__":
    main()
