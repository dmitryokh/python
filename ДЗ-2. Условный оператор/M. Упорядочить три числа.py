a = int(input())
b = int(input())
c = int(input())
if a <= b <= c:
    pass
elif a <= c <= b:
    a, b, c = a, c, b
elif b <= a <= c:
    a, b, c = b, a, c
elif b <= c <= a:
    a, b, c = b, c, a
elif c <= a <= b:
    a, b, c = c, a, b
else:
    a, b, c = c, b, a
print(a, b, c)
