import random
import string
from cryptography.fernet import Fernet

#Welcome messeage, introduction to program
print("Welcome to the Password Generator!")
user_choice = input("Press X to generate a password, Y to strengthen your current password, or Z to exit: ")

#password strengthening algorithim
def strengthen_password(password):
    if len(password) < 17: #Check the length, if less than 17 add randomm char up to 17
        for i in range(17 - len(password)):
            password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    
    tracker = [] #to keep track of capital letters
    for i in password: #Check amt of capital letters.
            if i in string.ascii_uppercase:
                tracker += i
    if len(tracker) < 3:
        #Capitalize 2 random letters due to it being less than 3
        password_list = list(password)
        count = 0
        for i in range(len(password_list)):
            if password_list[i] in string.ascii_lowercase and count < 2:
                password_list[i] = password_list[i].upper()
                count += 1
        password = ''.join(password_list)
    
    return password

# Algorithim to generate a random password
if user_choice == "X":
    print("Generating a random password...")
    password = ""
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







