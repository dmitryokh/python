n = int(input())
lst = list(map(int, input().split()))
x = int(input())
dif = 2001
sign = 0
for i in range(len(lst)):
    if abs(lst[i] - x) < dif:
        dif = abs(lst[i] - x)
        if lst[i] > x:
            sign = 1
        elif lst[i] < x:
            sign = -1
        else:
            sign = 0
print(x + sign * dif)
