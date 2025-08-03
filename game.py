from random import choice


def game():
    valid_choices = ['scissor', 'paper', 'rock']

    while True:
        choice_input = input(
            "Choose one (scissor, paper, rock): ").strip().lower()
        if choice_input in valid_choices:
            print(f"You chose: {choice_input}")
            break
        else:
            print("Invalid choice. Please try again.")

    random_choice = choice(valid_choices)
    print(f"Computer chose: {random_choice}")

    def winner(player, computer):
        if player == computer:
            return "It's a tie"
        elif (player == "rock" and computer == "scissor") or \
             (player == "scissor" and computer == "paper") or \
             (player == "paper" and computer == "rock"):
            return "You win"
        else:
            return "Computer wins"

    # Call and print the result
    result = winner(choice_input, random_choice)
    print(result)


game()
