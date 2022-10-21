DELTA = 0.000_000_0001

iterations = 0
x = float(input("Geben sie bitte eine Zahl ein: "))
counter = 0
z = x


def root():
    return z - ((z*z-x)/(2*z))


while (abs(root()-z)) > DELTA:
    counter += 1
    z = root()


print("RESULT: ", z)
print("ITERATIONS: ", counter)
print("PYTHON CLAIMS ROOT OF", x, "IS", z)
