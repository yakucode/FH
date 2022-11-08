# 5: Falsche Zuweisung eines Tupels
try:
    s, t = 3, 4, 12
    print(s, t)
except:
    print("Fehler")
# 6: Rest in Liste
print()
x, *y, z = 3, 5.2, "hallo", 7.3, 2.9
print(x)
print(y)
print(z)
