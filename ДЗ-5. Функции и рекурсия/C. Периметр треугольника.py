from math import sqrt


def distance(x1, y1, x2, y2):
    return(sqrt((x2 - x1)**2 + (y2 - y1)**2))

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

a = distance(x1, y1, x2, y2)
b = distance(x1, y1, x3, y3)
c = distance(x3, y3, x2, y2)

print(a + b + c)
