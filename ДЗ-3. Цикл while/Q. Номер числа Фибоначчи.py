a1 = 1
a0 = 1
a = int(input())
i = 3
if a == 0:
    print(0)
else:
    while a0 <= a:
        temp = a0
        a0 += a1
        a1 = temp
        i += 1
    if a == a1:
        print(i-2)
    else:
        print("-1")

