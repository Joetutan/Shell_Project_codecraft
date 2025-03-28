import sys


def main():
     #Uncomment this block to pass the first stage
     

     # Wait for user input
     #input()
     #read the command 
     while True:
        sys.stdout.write("$ ")

        if input() == "exit 0":
            break
        else:
            command = input()
            #print command recieved
            print(f"{command}: command not found")
        

        


if __name__ == "__main__":
    main()
