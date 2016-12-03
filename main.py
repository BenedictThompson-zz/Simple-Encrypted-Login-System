import time
import ast
import os
import getpass
from passlib.hash import pbkdf2_sha256
def refreshlist():
    infile = open('creds.cred', 'r')
    per_row = []

    for line in infile:
        per_row.append(line.strip().split('\t'))
    per_column = zip(*per_row)
    try:
        global firstname
        global username
        global usernames
        global password
        global nocontents
        firstnames = str(per_column[0])
        firstnames = firstnames.replace("(", "[")
        firstnames = firstnames.replace(")", "]")
        firstname = ast.literal_eval(firstnames)
        
        usernames = str(per_column[1])
        usernames = usernames.replace("(", "[")
        usernames = usernames.replace(")", "]")
        username = ast.literal_eval(usernames)
        
        passwords = str(per_column[2])
        passwords = passwords.replace("(", "[")
        passwords = passwords.replace(")", "]")
        password = ast.literal_eval(passwords)
        nocontents = 0
    except:
        nocontents = 1
        pass

refreshlist()
print "Welcome to the Simple Login System."
print "Your passwords are encrypted with SHA256."
print "Coded by Ben Thompson on 03/13/16"
time.sleep(0.2)
print "Do you want to:"
time.sleep(0.2)
print "[1]Create an account"
print "[2]Login to an account"
selection = input("What do you want to do (eg. 1 or 2)?: ")
accountcreation = 1
if selection == 1:
    while accountcreation == True:
        fullname = raw_input("What is your full name?: ")
        if fullname == "":
            print ("Please enter a name")
            continue
        else:
            a = 1
        while a == 1:
            Username = raw_input("Please enter a username: ")
            if nocontents == 0:
                if any(item.lower() == Username.lower() for item in usernames):
                    print ("Sorry, That username is taken, please enter another.")
                    continue
                elif Username == "":
                    print ("You need to enter a username!")
                    continue
            elif Username == "":
                print ("You need to enter a username!")
                continue
            #else:
            b = 1
            while b == 1:
                enteredpassword = getpass.getpass("Please enter a password: ")
                if enteredpassword == "":
                    print "You need to enter a password!"
                else:
                    print ("Creating the User. Please wait for a few moments")
                    password = pbkdf2_sha256.encrypt(enteredpassword, rounds=200000, salt_size=16)
                    tosavetofile = (fullname + "\t" + Username + "\t" + password)
                    credfile = open("creds.cred","a")
                    credfile.write(tosavetofile + "\n")
                    credfile.close()
                    print ("Done! Now taking you to login.")
                    time.sleep(0.25)
                    b = 0
                    a = 0
                    selection = 0
                    accountcreation = 0
                    os.system('cls')
                    refreshlist()
os.system('cls')
loginusername = raw_input("Please enter your username: ")
loginpassword = getpass.getpass("Please enter your password: ")
with open("creds.cred") as myFile:
    for num, line in enumerate(myFile, 1):
        if loginusername in line:
            dataloc = num - 1
pwdtoverify = password[dataloc]

verifypw = str(pbkdf2_sha256.verify(loginpassword, pwdtoverify))
if verifypw == "True":
    print ("Welcome " + firstname[dataloc])
    print "You have successfully logged in!"
    time.sleep(2)
else:
    print ("Incorrect username and password!")
    time.sleep(2)
