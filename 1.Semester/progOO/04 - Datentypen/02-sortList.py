def main():
    num = 0
    numList = []
    while not (num == "q"):
        num = input("enter whole numbers: ")

        if "." in num:
            print("only whole numbers!")
        else:

            try:
                wNum = int(num)
                numList.append(wNum)
                numList.sort()
            except:
                print("only numbers")

    print(numList)


main()
