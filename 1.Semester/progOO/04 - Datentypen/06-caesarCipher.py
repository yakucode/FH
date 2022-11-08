KEY = 2


def cypher(str, choice):
    # convert str to list for easy access
    strAr = list(str)
    cypherString = ""
    # iterate over chars in list and concat encoded char with cypherString var
    for x in range(len(strAr)):
        ch = strAr[x]
        chVal = ord(ch)
        aVal = ord("a")
        AVal = ord("A")
        # if true encodes user input
        if choice == 1:
            # differentiate between capital and lowercase letters
            if ch.isupper():
                cypherString += ((chr((((chVal-AVal)+KEY) % 26)+AVal)))
            else:
                cypherString += ((chr((((chVal-aVal)+KEY) % 26)+aVal)))
        # decodes user input
        elif choice == 2:
            if ch.isupper():
                cypherString += ((chr((((chVal-AVal)-KEY) % 26)+AVal)))
            else:
                cypherString += ((chr((((chVal-aVal)-KEY) % 26)+aVal)))
        else:
            print("something went wrong - try again")

    if choice == 1:
        print("your input encoded is: ", cypherString)
    else:
        print("your input decoded is: ", cypherString)

    return cypherString


def main():
    str = input("enter text: ")
    choice = int(input("enter 1 for encode - enter 2 for decode: "))

    if choice == 1 or choice == 2:
        if str.isalpha():
            cypher(str, choice)
        else:
            print("text may only contain letters - try again ")
    else:
        print("invalid input for choice - try again ")


main()
