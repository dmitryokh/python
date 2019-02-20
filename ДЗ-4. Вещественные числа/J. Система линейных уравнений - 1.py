a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if a != 0:
    y = (f - e * c / a) / (d - b * c / a)
    x = (e - b * y) / a
else:
    y = e/b
    x = (f - d*y)/c
print(x, y)
