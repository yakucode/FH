def reverse(str):
    rstr = ""
    rStrAr = []
    # iterate over every char and append to rStrAr list
    for word in str:
        for ch in word:
            rStrAr.append(ch)
    # reverse List
    rStrAr.reverse()

    # iterate over reversed list and add chars together to a string
    for ch in rStrAr:
        rstr += ch
    # return reversed string
    return rstr


def main():
    x = input("enter str to be reversed: ")
    print(f"your string in reverse is: \n" , reverse(x))


main()
