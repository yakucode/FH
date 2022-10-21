def bmiCalc(height, weight):
    """calculates and returns bmi"""
    height = float(height)
    weight = float(weight)
    return weight/((height/100)*2)


def bmiResult():
    """prints result based on calculated bmi"""
    height = input("enter height in cm: ")
    weight = input("enter weight in kg: ")
    bmi = round(bmiCalc(height, weight), 2)

    if bmi < 18.5:
        print("your bmi is:", bmi, "which is underweight")
    elif bmi >= 18.5 and bmi <= 25:
        print("your bmi is:", bmi, "which is normal")
    elif bmi >= 25:
        print("your bmi is:", bmi, "which is overweight")
    else:
        print("something went wrong")


def main():
    """main program"""
    bmiResult()


main()
