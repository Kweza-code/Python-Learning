from random import choice


def game():
    valid_choices = ['scissor', 'paper', 'rock']
    winnerComputer = 0
    winnerHuman = 0

    while winnerComputer < 3 and winnerHuman < 3:

        print("Choose your option")
        print("1 : scissor")
        print("2 : paper")
        print("3 : rock")

        while True:
            try:
                choice_number = int(input("Please enter a number 1, 2 or 3 :"))
                if choice_number in [1, 2, 3]:
                    player = valid_choices[choice_number - 1]
                    print(f"you picked {player}")
                    break
                else:
                    print("Invalid Number")

            except ValueError:
                print("Une erreur est survenu picked a number")

        computer = choice(valid_choices)
        print(f"Computer chose: {computer}")

        if player == computer:
            print("It's a tie!")
        elif (player == "rock" and computer == "scissor") or \
             (player == "scissor" and computer == "paper") or \
             (player == "paper" and computer == "rock"):
            winnerHuman += 1
            print("You win this round!")
        else:
            winnerComputer += 1
            print("Computer wins this round!")

        print(f"Score — You: {winnerHuman} | Computer: {winnerComputer}")
        print("-" * 30)

    if winnerHuman == 3:
        print("🎉 You won the game!")
    else:
        print("💻 Computer won the game!")


game()
