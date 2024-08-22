import string
import random

def start_pass_gen():
    print("************************")
    print("Password Generator")
    print("************************")
    print("Version : 1.0")
    print("************************")
    print("Made by Santhosh T")
    print("************************\n")
    input_len()

def input_len():
    global length
    
    try:
        length = int(input("Enter the length of the password to generate: "))
        pass_gen()
    except ValueError:
        print("\nWRONG INPUT!! PLEASE TRY AGAIN!!\n")
        input_len()

def pass_gen():
    randompass = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length))

    print("\nHere is the your random password : " +  randompass)
    exit_pass_gen()
    
def exit_pass_gen():
    print("")
    AskAgain = str(input("Do you want to do another password generation (Y/N): "))
    UppercaseAA = AskAgain.upper()
    
    if UppercaseAA == 'Y':
        print("\nRestarting the application...\n")
        start_pass_gen()
    elif UppercaseAA == 'N':
        print("\nPassword Generator Closed...!")
    else:
        print("\nWRONG INPUT!! PLEASE TRY AGAIN!!")
        exit_pass_gen()

start_pass_gen()
