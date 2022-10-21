def optiPulseCalc(age):
    return 165 - 0.75 * age


def optiPulseResult(pulse):

    print("optimal pulse:", pulse)


def main():
    age = float(input("age: "))
    optiPulseResult(optiPulseCalc(age), age)


main()
