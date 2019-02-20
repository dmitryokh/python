from math import sqrt

a = float(input())
b = float(input())
c = float(input())
if a == 0:
    if b == 0:
        if c == 0:
            print("3")
        else:
            print("0")
    else:
        print("1", c*(-1)/b)
else:
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (b * (-1) - sqrt(d)) / (2 * a)
        x2 = (b * (-1) + sqrt(d)) / (2 * a)
        print("2", min(x1, x2), max(x1, x2))
    elif d == 0:
        print("1", (b * (-1)) / (2 * a))
