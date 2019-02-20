lst = list(map(int, input().split()))
oddmin = 1001
for i in range(len(lst)):
    if lst[i] % 2 == 1 and lst[i] < oddmin:
        oddmin = lst[i]
print(oddmin)
