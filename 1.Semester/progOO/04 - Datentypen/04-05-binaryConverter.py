def binConv(bin):
    
    # typecast bin to list
    binAr = list(bin)

    # reverse binAr to start from lowest number and init decNum=0
    binAr.reverse()
    decNum = 0
    print(type(binAr[0]))

    # iterate over reversed binAr and perform arithmetic conversion to decimal number
    for x in range(len(binAr)):
        decNum += int(binAr[x])*2**x

    return decNum


def main():
    bin = input("enter binary number: ")
    print(binConv(bin))


main()
