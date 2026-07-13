# ==========================================================
# W03 Project: Adventure Game
# Author: Evelyn Akpan
#
# Description:
# In this adventure game, you are searching for the legendary
# Crystal of Destiny. Every decision changes your journey,
# leading to different adventures and endings.
#
# Creativity:
# I added three different starting paths, multiple winning
# endings, and several unique game-over endings to make the
# adventure more exciting and replayable.
# ==========================================================

print("========================================")
print("     THE QUEST FOR THE CRYSTAL")
print("========================================")
print("You are an explorer searching for the legendary Crystal of Destiny.")
print("Your journey begins at the edge of a mysterious land.\n")

choice1 = input("Do you travel through the FOREST, CAVE, or RIVER? ").lower()

# ---------------- FOREST ----------------
if choice1 == "forest":
    print("\nYou enter the forest and hear strange sounds.")

    choice2 = input("Do you FOLLOW the sound or CLIMB a tree? ").lower()

    if choice2 == "follow":
        print("\nYou discover a wounded unicorn.")

        choice3 = input("Do you HELP the unicorn or LEAVE it? ").lower()

        if choice3 == "help":
            print("\nThe unicorn rewards you with the Crystal of Destiny.")
            print("Congratulations! YOU WIN!")
        elif choice3 == "leave":
            print("\nThe forest becomes cursed and you cannot escape.")
            print("GAME OVER!")
        else:
            print("\nInvalid choice. The unicorn disappears.")
            print("GAME OVER!")

    elif choice2 == "climb":
        print("\nFrom the top of the tree, you spot an old rope bridge.")

        choice3 = input("Do you CROSS the bridge or GO BACK? ").lower()

        if choice3 == "cross":
            print("\nYou safely cross and discover the hidden Crystal.")
            print("YOU WIN!")
        elif choice3 == "go back":
            print("\nYou become lost in the forest forever.")
            print("GAME OVER!")
        else:
            print("\nInvalid choice. You fall from the tree.")
            print("GAME OVER!")

    else:
        print("\nInvalid choice. The forest spirits send you home.")
        print("GAME OVER!")

# ---------------- CAVE ----------------
elif choice1 == "cave":
    print("\nThe cave is dark and cold.")

    choice2 = input("Do you LIGHT a torch or WALK in the dark? ").lower()

    if choice2 == "light":
        print("\nThe light reveals an ancient wizard.")

        choice3 = input("Do you TALK to the wizard or IGNORE him? ").lower()

        if choice3 == "talk":
            print("\nThe wizard gives you the Crystal of Destiny.")
            print("YOU WIN!")
        elif choice3 == "ignore":
            print("\nWithout the wizard's help, you cannot escape the cave.")
            print("GAME OVER!")
        else:
            print("\nInvalid choice. The wizard disappears.")
            print("GAME OVER!")

    elif choice2 == "walk":
        print("\nYou hear footsteps behind you.")

        choice3 = input("Do you RUN or HIDE? ").lower()

        if choice3 == "run":
            print("\nYou escape safely, but without the Crystal.")
            print("GAME OVER!")
        elif choice3 == "hide":
            print("\nA giant spider finds you.")
            print("GAME OVER!")
        else:
            print("\nInvalid choice. You get lost forever.")
            print("GAME OVER!")

    else:
        print("\nInvalid choice. You remain trapped in the cave.")
        print("GAME OVER!")

# ---------------- RIVER ----------------
elif choice1 == "river":
    print("\nYou arrive at a wide river.")

    choice2 = input("Do you SWIM across or BUILD a raft? ").lower()

    if choice2 == "swim":
        print("\nHalfway across, you find a treasure chest.")

        choice3 = input("Do you OPEN it or IGNORE it? ").lower()

        if choice3 == "open":
            print("\nInside is the Crystal of Destiny!")
            print("YOU WIN!")
        elif choice3 == "ignore":
            print("\nYou safely reach the other side, but miss the treasure.")
            print("GAME OVER!")
        else:
            print("\nInvalid choice. The current carries you away.")
            print("GAME OVER!")

    elif choice2 == "build":
        print("\nYour raft reaches a mysterious island.")

        choice3 = input("Do you EXPLORE the island or RETURN home? ").lower()

        if choice3 == "explore":
            print("\nYou discover the Crystal hidden in an ancient temple!")
            print("YOU WIN!")
        elif choice3 == "return home":
            print("\nYou return home safely without the Crystal.")
            print("GAME OVER!")
        else:
            print("\nInvalid choice. Your raft sinks.")
            print("GAME OVER!")

    else:
        print("\nInvalid choice. The river current sweeps you away.")
        print("GAME OVER!")

# ---------------- INVALID FIRST CHOICE ----------------
else:
    print("\nInvalid choice.")
    print("Please restart the game and choose FOREST, CAVE, or RIVER.")