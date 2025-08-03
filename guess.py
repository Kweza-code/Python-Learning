from random import *

def game():
    randomNumber = randint(1, 50)
    attempts = 0
    found = False

    while not found:
        try:
            randomHuman = int(input("Enter a number between 1 and 50: "))
            attempts += 1

            if randomHuman < randomNumber:
                print("Trop petit !")
            elif randomHuman > randomNumber:
                print("Trop grand !")
            else:
                print(f"Bravo ! Tu as trouvé le nombre {randomNumber} en {attempts} essais.")
                found = True
        except ValueError:
            print("❌ Tu dois entrer un nombre valide.")

# Lancer le jeu
game()