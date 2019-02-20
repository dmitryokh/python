a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
if a1 <= b1 <= c1:
    a1 += 0
elif a1 <= c1 <= b1:
    temp = c1
    c1 = b1
    b1 = temp
elif b1 <= a1 <= c1:
    temp = a1
    a1 = b1
    b1 = temp
elif b1 <= c1 <= a1:
    temp = a1
    a1 = b1
    b1 = c1
    c1 = temp
elif c1 <= a1 <= b1:
    temp = a1
    a1 = c1
    c1 = b1
    b1 = temp
else:
    temp = a1
    a1 = c1
    c1 = temp

if a2 <= b2 <= c2:
    b1 += 0
elif a2 <= c2 <= b2:
    temp = c2
    c2 = b2
    b2 = temp
elif b2 <= a2 <= c2:
    temp = a2
    a2 = b2
    b2 = temp
elif b2 <= c2 <= a2:
    temp = a2
    a2 = b2
    b2 = c2
    c2 = temp
elif c2 <= a2 <= b2:
    temp = a2
    a2 = c2
    c2 = b2
    b2 = temp
else:
    temp = a2
    a2 = c2
    c2 = temp

ab = bc = ac = 0

if ((a1 < a2) and (b1 > b2)) or ((a1 > a2) and (b1 < b2)):
    ab = 1
if ((c1 < c2) and (b1 > b2)) or ((c1 > c2) and (b1 < b2)):
    bc = 1
if ((c1 < c2) and (a1 > a2)) or ((c1 > c2) and (a1 < a2)):
    ac = 1

if (a1 == a2) and (b1 == b2) and (c1 == c2):
    print("Boxes are equal")
elif (ac == 1) or (bc == 1) or (ab == 1):
    print("Boxes are incomparable")
elif (a1 <= a2) and (b1 <= b2) and (c1 <= c2):
    print("The first box is smaller than the second one")
elif (a1 >= a2) and (b1 >= b2) and (c1 >= c2):
    print("The first box is larger than the second one")
else:
    print("Boxes are incomparable")
