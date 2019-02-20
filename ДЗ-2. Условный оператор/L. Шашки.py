x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (abs(x2 - x1) + abs(y2 - y1)) % 2 != 0:
    print("NO")
elif ((x2 - y2) > (y1 - y1)) or ((y2 + x2) < (y1 + x1)):
    print("NO")
else:
    print("YES")
