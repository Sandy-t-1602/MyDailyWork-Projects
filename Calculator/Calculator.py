import sys

def exit_calc():
    d = str(input("Do you want to do another calculation(Y/N): "))
    e = d.upper()
    if e == 'Y':
        print("")
        print("Restarting Calculator...\n")
        start_calc()
    elif e == 'N':
        print("\nCalculator Closed!")
        sys.exit()
    else:
        print("\nWRONG INPUT! PLEASE TRY AGAIN!\n")
        exit_calc()

def start_calc():
    print("*************************")
    print("Calculator")
    print("*************************")
    print("Version : 1.0")
    print("*************************")
    print("Made by Santhosh T")
    print("*************************\n")
    input_num()

def input_num():

    global a
    global b
    
    try:
        a = int(input("Enter 1st Number: "))
        b = int(input("Enter 2nd Number: "))
        print("")
    except ValueError:
        print("\nDATA TYPE ERROR!! PLEASE INPUT AN INTEGER VALUE!!\n")
        print("Restarting Calculator...\n")
        start_calc()
    calc()

def calc():
    try:
        print("1 - Addition")
        print("2 - Subtraction")
        print("3 - Multiplication")
        print("4 - Division (Quotient)")
        print("5 - Division (Remainder)\n")
        c = int(input("Choose the mode of arithmetic option: "))
    
        if c == 1:
            print("\nThe sum of", a, "and", b, "is", a+b, "\n")
            exit_calc()
        elif c == 2:
            print("\nThe difference between", a, "and", b, "is", a-b, "\n")
            exit_calc()
        elif c == 3:
            print("\nThe product of", a, "and", b, "is", a*b,  "\n")
            exit_calc()
        elif c == 4:
            print("\nThe Quotient obtained by dividing", a, "and", b, "is", a/b, "\n")
            exit_calc()
        elif c == 5:
            print("\nThe Remainder obtained by dividing ", a, "and", b, "is", a%b, "\n")
            exit_calc()
        else:
            print("\nWRONG INPUT! PLEASE TRY AGAIN!\n")
            calc()
    except ValueError:
        print("\nDATA TYPE ERROR!! PLEASE INPUT AN INTEGER VALUE!!\n")
        calc()

start_calc()
