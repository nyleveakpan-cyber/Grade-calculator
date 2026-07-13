# =====================================================
# Adventure Game: The Lost Temple
# Author: Evelyn Sunday Akpan
#
# Description:
# This is a text-based adventure game where the player
# explores a mysterious temple in search of a legendary
# crystal. Every path has three levels of choices, and
# different choices lead to different endings.
#
# Creativity:
# - More than two choices in the first scenario.
# - Multiple unique endings.
# - Case-insensitive user input using .lower().
# =====================================================

print("=====================================")
print("     THE LOST TEMPLE ADVENTURE")
print("=====================================")
print("You are an explorer searching for the legendary Crystal of Light.")
print("You arrive at the entrance of an ancient temple.")

choice1 = input("\nDo you enter through the FRONT, SIDE, or BACK entrance? ").lower()

# ------------------ FRONT ------------------
if choice1 == "front":
    print("\nYou walk through the front entrance and see two stairways.")

    choice2 = input("Do you go UPSTAIRS or DOWNSTAIRS? ").lower()

    if choice2 == "upstairs":
        print("\nUpstairs you find a sleeping dragon guarding a treasure.")

        choice3 = input("Do you FIGHT the dragon or SNEAK past it? ").lower()

        if choice3 == "fight":
            print("\nThe dragon is too powerful. You fought bravely but lost.")
            print("GAME OVER!")
        elif choice3 == "sneak":
            print("\nYou quietly sneak past the dragon and claim the Crystal!")
            print("Congratulations! YOU WIN!")
        else:
            print("\nInvalid choice. The dragon wakes up and chases you away.")
            print("GAME OVER!")

    elif choice2 == "downstairs":
        print("\nDownstairs you discover a flooded tunnel.")

        choice3 = input("Do you SWIM across or BUILD a raft? ").lower()

        if choice3 == "swim":
            print("\nYou safely swim across and discover hidden treasure!")
            print("YOU WIN!")
        elif choice3 == "build":
            print("\nYour raft falls apart and you drift out of the temple.")
            print("GAME OVER!")
        else:
            print("\nInvalid choice. You become trapped in the tunnel.")
            print("GAME OVER!")

    else:
        print("\nInvalid choice. You get lost inside the temple.")
        print("GAME OVER!")

# ------------------ SIDE ------------------
elif choice1 == "side":
    print("\nYou enter through the side entrance and find a mysterious garden.")

    choice2 = input("Do you PICK a flower or FOLLOW a glowing butterfly? ").lower()

    if choice2 == "pick":
        print("\nThe flower releases sleeping gas.")

        choice3 = input("Do you WAIT or RUN? ").lower()

        if choice3 == "wait":
            print("\nThe gas disappears, and you safely continue to the treasure.")
            print("YOU WIN!")
        elif choice3 == "run":
            print("\nYou trip and fall into a hidden pit.")
            print("GAME OVER!")
        else:
            print("\nInvalid choice. You fall asleep forever.")
            print("GAME OVER!")

    elif choice2 == "follow":
        print("\nThe butterfly leads you to a magical bridge.")

        choice3 = input("Do you CROSS the bridge or TURN BACK? ").lower()

        if choice3 == "cross":
            print("\nThe bridge leads directly to the Crystal of Light.")
            print("YOU WIN!")
        elif choice3 == "turn back":
            print("\nYou leave the temple safely, but without the treasure.")
            print("GAME OVER!")
        else:
            print("\nInvalid choice. The bridge disappears.")
            print("GAME OVER!")

    else:
        print("\nInvalid choice. Thorny vines trap you.")
        print("GAME OVER!")

# ------------------ BACK ------------------
elif choice1 == "back":
    print("\nThe back entrance leads to a dark cave.")

    choice2 = input("Do you LIGHT a torch or WALK in the dark? ").lower()

    if choice2 == "light":
        print("\nThe torch reveals an old wizard.")

        choice3 = input("Do you TALK to the wizard or IGNORE him? ").lower()

        if choice3 == "talk":
            print("\nThe wizard gives you a magic key to unlock the Crystal.")
            print("YOU WIN!")
        elif choice3 == "ignore":
            print("\nWithout the wizard's help, you cannot open the treasure room.")
            print("GAME OVER!")
        else:
            print("\nInvalid choice. The wizard disappears.")
            print("GAME OVER!")

    elif choice2 == "walk":
        print("\nYou hear strange noises in the darkness.")

        choice3 = input("Do you KEEP WALKING or GO BACK? ").lower()

        if choice3 == "keep walking":
            print("\nYou fall into a deep hole.")
            print("GAME OVER!")
        elif choice3 == "go back":
            print("\nYou safely escape the cave but never find the Crystal.")
            print("GAME OVER!")
        else:
            print("\nInvalid choice. You get lost forever.")
            print("GAME OVER!")

    else:
        print("\nInvalid choice. You cannot find your way.")
        print("GAME OVER!")

# ------------------ INVALID FIRST CHOICE ------------------
else:
    print("\nInvalid entrance choice.")
    print("Please restart the game and choose FRONT, SIDE, or BACK.")