import random
import string
from SavingData import *

#Welcome messeage, introduction to program
print("Welcome to the Password Generator!")

while True:
    user_choice = input("Press X to generate a password, Y to strengthen your current password, or Z to exit: ").upper()
    password = ""  # Initialize password variable

    #password strengthening algorithim
    def strengthen_password(password):
        new_password = ''
        if len(password) < 17: #Check the length, if less than 17 add randomm char up to 17
            new_password = password
            for i in range(17 - len(password)):
                new_password += random.choice(string.ascii_letters + string.digits + string.punctuation)
        else:
            new_password = password
        
        # Character replacement for all passwords regardless of length
        temp_password = ''
        for i in new_password:
            if i == "a" or i == "A":
                temp_password += "@"
            elif i == "s" or i == "S":
                temp_password += "$"
            elif i == "p" or i == "P":
                temp_password += "9"
            elif i == "o" or i == "O":
                temp_password += "0"
            elif i == "c" or i == "C":
                temp_password += "("
            elif i == "g" or i == "G":
                temp_password += "%"
            elif i == "r" or i == "R":
                temp_password += "?"
            else:
                temp_password += i
        
        new_password = temp_password
        
        tracker = [] #to keep track of capital letters
        for i in new_password: #Check amt of capital letters.
                if i in string.ascii_uppercase:
                    tracker += i
        if len(tracker) < 3:
            #Capitalize 2 random letters due to it being less than 3
            password_list = list(new_password)
            count = 0
            for i in range(len(password_list)):
                if password_list[i] in string.ascii_lowercase and count < 2:
                    password_list[i] = password_list[i].upper()
                    count += 1
            new_password = ''.join(password_list)
        
        return new_password

    # Algorithim to generate a random password
    if user_choice == "X":
        print("Generating a random password...")
        for i in range(17):
            password += random.choice(string.ascii_letters + string.digits + string.punctuation)
        print(f'Your password is: {password}')

    # process to strengthen the password
    elif user_choice == "Y":
        password = input("Enter your password: ")
        password = strengthen_password(password)
        print(f'Your new password is: {password}')
    elif user_choice == "Z":
        exit()
    else:
        print("Invalid option. Please try again.")
        continue  # Skip saving if invalid option

    #Ask user if they want to save their password. If they do, ask for a username and save to passwords.json
    if password:  # Only ask to save if we have a password
        save_password = input("Do you want to save your password? (Y/N): ").upper()
        if save_password == "Y":
            username = input("Enter a username: ")
            saving_data = SavingData(username, password)
            saving_data.save_password()
            print("Password saved successfully.")
        elif save_password == "N":
            print("Password not saved.")
        else:
            print("Invalid option. Please try again.")
            
    #this is a test to see if user can access their password
    password_finder = input("Would you like to access your password? (Y/N): ").upper()
    if password_finder == "Y":
        username = input("Enter your username: ")
        accessing_data = accessingData(username)
        print(accessing_data.access_password())
    elif password_finder == "N":
        print("Password not accessed.")
    else:
        print("Invalid option. Please try again.")






