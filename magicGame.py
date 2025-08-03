from random import choice


def game():
    item = ["fire", "water", "wind"]
    scoreHuman = 0
    scoreComputer = 0

    while scoreHuman < 3 and scoreComputer < 3:

        print("Choose your card")
        print("1 = fire")
        print("2 = water")
        print("3 = wind")

        while True:
            try:
                choice_number = int(input("Enter 1, 2 or 3 : "))
                if choice_number in [1, 2, 3]:
                    player = item[choice_number - 1]
                    print(f"You picked: {player}")
                    break
                else:
                    print("Invalid number please enter 1,2 or 3")
            except ValueError:
                print("Please enter a valid number")

        computer = choice(item)
        print(f"Computer picked : {computer}")

        if computer == player:
            print("Vous avez choisi les deux élement")
        elif (player == "water" and computer == "fire") or \
             (player == "wind" and computer == "water") or \
             (player == "fire" and computer == "wind"):
            scoreHuman += 1
            print("Tu as gagner un point")
        else:
            scoreComputer += 1
            print("l'ordinateur à gagner un point")

        print(f"Score — You: {scoreHuman} | Computer: {computer}")
        print("-" * 30)

    if scoreHuman == 3:
        print("Tu as gagné la partie")
    else:
        print("l'ordinateur à gagné la partie")


game()
