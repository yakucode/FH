# get curr date from user
day = int(input("Tag: "))
month = int(input("Monat: "))

if month == 2 and day > 29:
    print("feb only 29 days")
elif month == (1 or 3 or 5 or 7 or 8 or 10 or 12) and day > 31:
    print("Month ", month, "has less than 32 days")
elif month == (4 or 6 or 9 or 11) and day > 30:
    print("Month ", month, "has less than 31 days")
elif month < 1 and month > 12:
    print("invalid month")
elif month == 1:
    print("Tage seit Jahresanfang: ", day)
else:
    days = 0
    for x in range(month):

        if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
            days += 31
        elif x == 2:
            days += 28
        elif x == 4 or x == 6 or x == 9 or x == 11:
            days += 30
    print("Tage seit Jahresanfang: ", days+day)
