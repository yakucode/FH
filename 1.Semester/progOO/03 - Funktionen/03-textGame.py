def caveChoice():
    choice = int(input("Cave 1 or 2?"))
    while choice != 1 and choice != 2:
        choice = int(input("invalid choice! Enter 1 or 2: "))

    if choice == 1:
        print("You find a cave full of treasure!")
    elif choice == 2:
        print("A dragon devours you! RIP")


def contChoice():
    choice = input("play again? YES / NO: ")
    while choice != "YES" and choice != "NO":
        choice = input("invalid choice! Enter YES or NO ")
    return choice


def main():
    print("STARTING GAME")
    playing = True

    while playing == True:

        print("You are in a land of dragons, standing infront of two caves. Which cave do you choose?")

        caveChoice()

        cont = contChoice()
        if cont == "YES":
            playing = True
        elif cont == "NO":
            playing = False
        else:
            print("Ups something went wrong ...")

    print("GAME CLOSED - GOODBYE")


main()
