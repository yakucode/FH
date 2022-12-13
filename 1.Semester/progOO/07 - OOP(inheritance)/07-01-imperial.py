class Length:
    __foot = 0
    __inch = 0

    def __init__(self, foot, inch):

        if foot > 0:
            self.__foot = foot
        else:
            self.__foot = abs(foot)

        if inch < 12 and inch >= 0:
            self.__inch = inch
        elif inch >= 12:
            self.__foot += inch // 12
            self.__inch = inch % 12
        elif inch < 0 and inch > -12:
            self.__inch = abs(inch)
        elif inch <= -12:
            self.__foot += abs(inch) // 12
            self.__inch = abs(inch) % 12
        else:
            print("something went wrong")

    def __str__(self):
        return (
            f"current length is: {self.__foot} foot/feet and {self.__inch} inch(es)")

    def __add__(self, x):
        sum = Length(self.__foot, self.__inch)
        sum.__foot += x.__foot
        if sum.__inch + x.__inch >= 12:
            sum.__foot += (sum.__inch + x.__inch) // 12
            sum.__inch = (sum.__inch + x.__inch) % 12
        elif sum.__inch + x.__inch < 12:
            sum.__inch += x.__inch
        else:
            print("something went wrong with add method")
        return sum

    def __sub__(self, x):
        dif = Length(self.__foot, self.__inch)
        dif.__foot -= x.__foot
        if dif.__inch - x.__inch < 0:
            dif.__foot -= 1
            dif.__inch = 12 - x.__inch
        elif dif.__inch - x.__inch >= 0:
            dif.__inch -= x.__inch
        else:
            print("something went wrong with sub method")
        return dif


def main():
    len1 = Length(4, 2)
    len2 = Length(0, 3)
    len3 = len1 - len2
    print(len3)


main()
