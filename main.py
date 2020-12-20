import os.path

# check to see if the file exists, if it doesn't
# then create the file and write to it => 'w'
def checkFreq():
    if os.path.exists("info.txt"):
        pass
    else:
        file = open("info.txt", 'w')
        file.close()

# add a new entry to the main file
def appendNew():

    file = open("info.txt", 'a')
    
    print()
    
    website = input("Please enter the service name here: ")
    userName = input("Please enter the username here: ")
    password = input("Please enter the password here: ")
    
    print()

    un = "Username: " + userName + "\n"
    pw = "Password: " + password + "\n"
    web = "Service / Website: " + website + "\n"

    file.write("---------------------------------\n")
    file.write(un)
    file.write(pw)
    file.write(web)
    file.write("---------------------------------\n")
    file.write("\n")
    file.close

# read out the file
def readPw():
    file = open("info.txt", 'r')
    content = file.read()
    file.close()

    print(content)

# main function to run everything and asks if 
# ------ the user wants to re-run the program
def main():
    checkFreq()
    appendNew()
    readPw()

    temp = input("Do you want to run the program again? (True or False): ")

    if temp == "True" or temp == "T" or temp == "t":
        main()
    else:
        pass

main()
