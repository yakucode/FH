
def main():

    warenlager = {}

    weiter = True

    while weiter == True:

        name = input("warenname: (q für Ende)")

        if name != "q":

            preis = input("preis")
            try:
                preis = float(preis)
                warenlager[name] = preis
            except:
                pass
        else:
            weiter = False

    price = 0

    for product in warenlager:
        amount = int(input(f"how many  {product} s would you like?"))
        price += amount * warenlager.get(product)

    print("total is: ", price)


main()
