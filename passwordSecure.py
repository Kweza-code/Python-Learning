import getpass


def validPassword (password):
    hasUpper = False 
    specialChar = 0
    number = 0


    for char in password :
        if char.isupper() :
            hasUpper = True
        if char in "!@#$%^&*()_+" :
            specialChar += 1
        if char.isdigit() :
            number += 1
    
    if hasUpper and specialChar >= 3 and number >= 3:
        return True
    else : 
        return False


def main():


    name = input("Enter your username: ")
    while True :
        password = getpass.getpass("Enter a password with 3 Char, 3 numbers and one Maj :")
        if validPassword(password) :
            print("Password Valid")
            break
        else :
            print("The password is not valid follow the instruction")



    while True:
        connectName = input("Enter your username again to connect: ")
        correctPassword = getpass.getpass("Enter your password again to connect: ")
        
        if connectName == name and correctPassword == password:
            print("✅ Access granted!")
            break
        else:
            print("❌ Incorrect login. Please try again.")

main()

