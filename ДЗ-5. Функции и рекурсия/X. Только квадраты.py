from math import sqrt

count = 0

def backsq(a):
    if int(a) != 0:
        a = int(input())
        backsq(a)
        if sqrt(a) == int(sqrt(a)) and a != 0:
            count += 1
            print(a, " ", sep="", end="")

a1 = int(input())
a = a1
backsq(a)
if sqrt(a1) == int(sqrt(a1)):
    print(a1)
    count += 1
print(count)
if count == 0:
    print(count)
