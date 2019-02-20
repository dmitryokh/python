a1 = 1
a0 = 1
n = int(input())
i = 3
if n == 0:
    a0 = 0
elif n == 1:
    a0 = 1
elif n == 2:
    a0 = 1
else:
    while i <= n:
        temp = a0
        a0 += a1
        a1 = temp
        i += 1
print(a0)
