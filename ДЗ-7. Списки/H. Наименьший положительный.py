lst = list(map(int, input().split()))
posmin = 1001
for i in range(len(lst)):
    if lst[i] > 0 and lst[i] < posmin:
        posmin = lst[i]
print(posmin)
