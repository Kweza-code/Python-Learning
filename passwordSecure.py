import getpass


def valid_password(password):
    has_upper = False
    special_char = 0
    number = 0

    for char in password:
        if char.isupper():
            has_upper = True
        if char in "!@#$%^&*()_+":
            special_char += 1
        if char.isdigit():
            number += 1

    if has_upper and special_char >= 3 and number >= 3 and len(password) > 6:
        return True
    else:
        return False


def main():
    name = input("Enter your username: ")

    while True:
        password = getpass.getpass(
            "Enter a password with 3 special characters, 3 numbers, one uppercase letter and lenght superior of 4: "
        )
        if valid_password(password):
            print("Password Valid")
            break
        else:
            print("The password is not valid. Please follow the instructions.")

    while True:
        connect_name = input("Enter your username again to connect: ")
        correct_password = getpass.getpass(
            "Enter your password again to connect: ")

        if connect_name == name and correct_password == password:
            print("✅ Access granted!")
            break

        else:
            print("❌ Incorrect login. Please try again.")


main()
