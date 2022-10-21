curNum = -99999999999999999
maxNum = curNum
while type(curNum) == int:
    x = input("enter a natural number: ")
    try:
        curNum = int(x)
    except:
        break
    if curNum > maxNum:
        maxNum = curNum
print("Highest number was: ", maxNum)
