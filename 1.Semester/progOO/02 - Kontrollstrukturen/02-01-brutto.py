# this program calculates tax stuff
brutto = float(input("Geben Sie Ihr Bruttgehalt in Euro ein:"))
if brutto > 2500:
    print("Es ergibt sich ein Steuerbetrag von: ", brutto*0.22, " Euro")
else:
    print("Es ergibt sich ein Steuerbetrag von: ", brutto*0.18, " Euro")
