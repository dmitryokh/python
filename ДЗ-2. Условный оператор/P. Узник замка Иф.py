a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
xy = xz = yz = 0
if ((a <= d) and (b <= e)) or ((a <= e) and (b <= d)):
    xy = 1
if ((a <= d) and (c <= e)) or ((c <= d) and (a <= e)):
    xz = 1
if ((c <= d) and (b <= e)) or ((b <= d) and (c <= e)):
    yz = 1
if xy == 1 or xz == 1 or yz == 1:
    print("YES")
else:
    print("NO")
