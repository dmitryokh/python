a = int(input())
b = int(input())
c = int(input())
if (a >= b + c) or (b >= a + c) or (c >= a + b):
    print("impossible")
elif (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == a**2 + b**2):
    print("rectangular")
elif (a**2 < b**2 + c**2) and (b**2 < a**2 + c**2) and (c**2 < a**2 + b**2):
    print("acute")
else:
    print("obtuse")
