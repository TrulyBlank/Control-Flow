# Proggramer: Ryan Gale
# Date: 10-11-21
# program: ATM Bank Transaction
"""
This program simulates an ATM utilizing If, Elif, and Else statements.
Nesting If statements and refresh our Comparison & Logical Operators.
"""

print("Welcome to Cash-R-Us Bank\nLet's take a moment to set up your account.\n")

# Set up account by asking users for their fist and last names using Variable.
first_name = input("What is your First name: ")
Last_Name = input("What is your Last name: ")

print("\nHey! Welcome to Cash-R-Us", first_name,Last_Name + ", we will now set up a security pin on your account . \n")

# Set up a PIN - Personal Identification Number
pin = input ("Please Choose a Four Digit Personal Identification Number: ")

print ("\n Thank You",first_name + ", we see that you set your PIN to",pin)


print("\nWould you like to make a transaction through our Automated Teller Machine")

ATM = input("Yes or No: ").lower()

if ATM == "yes":
    print("\n*******************************************\n")

    # This part of the program will be asking users to complete a transaction though the ATM
    print("Please insert your ATM card\n")
    print("Welcome to Cash-R-Us ATM",first_name,Last_Name,"\n")
    userPIN = input("What is your four diget PIN: ")

    if pin == userPIN:
        balance = 674
        print("\nYour Balance: $" + str(balance))
        
        
        typeOfTranscation = input("\nWould you like to make a Withdrawl or a Deposit\nW = Withdrawl or D = Deposit: ").lower()
        if typeOfTranscation =="w":
            withdralAmmount = int(input("Enter Ammount Of withdrawl ; "))
            balance = balance - withdralAmmount 
            print("your New Balance is $" + str(balance))
           

    else:
        print("Sorry", first_name,last_name,"your PIN doesn't match our records")




else:
    print("\nHave a Great Day!",first_name, Last_Name + ", please visit again soon ;)")
