a = int(input())
b = int(input())
c = int(input())
d = int(input())
if c != 0:
    imp = d*(-1)/c
if a != 0:
    x = b*(-1)/a
if a == 0 and c == 0:
    if d == 0:
        print("NO")
    elif b == 0:
        print("INF")
elif a == 0:
    if b == 0:
        print("INF")
    else:
        print("NO")
elif c == 0:
    if d == 0:
        print("NO")
    else:
        if (int(x) == x):
            print(int(x))
        else:
            print("NO")
elif x == imp:
    print("NO")
else:
    if (int(x) == x):
        print(int(x))
    else:
        print("NO")
