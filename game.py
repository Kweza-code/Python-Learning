from random import choice


def game():
    valid_choices = ['scissor', 'paper', 'rock']
    winnerComputer = 0
    winnerHuman = 0

    while winnerComputer < 3 and winnerHuman < 3:

        while True:
            player = input(
                "Choose one (scissor, paper, rock): ").strip().lower()
            if player in valid_choices:
                print(f"You chose: {player}")
                break
            else:
                print("Invalid choice. Please try again.")

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
