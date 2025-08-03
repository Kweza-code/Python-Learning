from random import choice, randint


def game():
    item = ["fire", "water", "wind"]
    scoreHuman = 0
    scoreComputer = 0

    while scoreHuman < 3 and scoreComputer < 3:

        print("🃏 Choisis ta carte :")
        print("1 = fire")
        print("2 = water")
        print("3 = wind")

        while True:
            try:
                choice_number = int(input("Entre 1, 2 ou 3 : "))
                if choice_number in [1, 2, 3]:
                    player = item[choice_number - 1]
                    print(f"Tu as choisi : {player}")
                    break
                else:
                    print("Numéro invalide. Choisis 1, 2 ou 3.")
            except ValueError:
                print("Erreur : entre un nombre valide.")

        computer = choice(item)
        print(f"L'ordinateur a choisi : {computer}")

        if computer == player:
            print("⚔️ Égalité ! Vous avez choisi le même élément.")
        elif (player == "water" and computer == "fire") or \
             (player == "wind" and computer == "water") or \
             (player == "fire" and computer == "wind"):
            scoreHuman += 1
            print("✅ Tu as gagné 1 point !")
        else:
            scoreComputer += 1
            print("❌ L'ordinateur a gagné 1 point !")

        # 💀 Potion empoisonnée pour le joueur
        potion_chance_human = randint(1, 5)
        if potion_chance_human == 1 and scoreHuman > 0:
            scoreHuman -= 1
            print("🧪 Tu as reçu une potion empoisonnée ! -1 point.")
        elif potion_chance_human == 1 and scoreHuman == 0:
            print("🧪 Tu as évité une potion... mais tu n'avais aucun point à perdre.")

        # 💀 Potion empoisonnée pour l'ordinateur
        potion_chance_computer = randint(1, 5)
        if potion_chance_computer == 1 and scoreComputer > 0:
            scoreComputer -= 1
            print("🧪 L'ordinateur a été empoisonné ! -1 point.")
        elif potion_chance_computer == 1 and scoreComputer == 0:
            print("🧪 L'ordinateur a reçu une potion... mais il n'avait aucun point.")

        # Affichage du score
        print(f"🎯 Score — Toi : {scoreHuman} | Ordinateur : {scoreComputer}")
        print("-" * 40)

    # Résultat final
    if scoreHuman == 3:
        print("🏆 Tu as gagné la partie ! Bravo !")
    else:
        print("💻 L'ordinateur a gagné la partie... réessaie !")


# Lancer le jeu
game()
