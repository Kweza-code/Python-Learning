from random import *


def player_choice():
    valid_choices = ['scissor', 'paper', 'rock']
    while True:
        choice = input("Choose one (scissor, paper, rock): ").strip().lower()
        if choice in valid_choices:
            print(f"You choose: {choice}")
            break
        else:
            print("Invalid choice. Please try again ")


player_choice()
