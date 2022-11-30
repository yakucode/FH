def numOfWords(sentence):
    sList = sentence.split()
    return len(sList)


def avgLen(sentence):
    sList = sentence.split()
    start = 0
    for element in sList:
        start += len(element)
    return start/len(sList)


def main():
    text = input("enter any sentence ")

    print("your sentence has: ", numOfWords(text), " words")
    print("average word length: ", avgLen(text))


main()
