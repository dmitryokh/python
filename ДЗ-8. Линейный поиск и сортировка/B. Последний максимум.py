lst = list(map(int, input().split()))
maxm = lst[0]
maxnum = 0
for i in range(len(lst)):
    if lst[i] > maxm:
        maxm = lst[i]
        maxnum = i
    elif lst[i] == maxm:
        maxnum = i
print(maxm, maxnum)
