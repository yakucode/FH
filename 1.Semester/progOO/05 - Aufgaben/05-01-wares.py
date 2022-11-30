warenlager = {'Butter': 1.90,
              'Brot': 2.30,
              'Schokolade': 1.50,
              'Apfel': 1.20}


def main():

    price = 0

    for product in warenlager:
        amount = int(input(f"how many  {product} s would you like?"))
        price += amount * warenlager.get(product)

    print("total is: ", price)


main()
