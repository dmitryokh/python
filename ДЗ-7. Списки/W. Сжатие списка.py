lst = list(map(int, input().split()))
point = 0
for i in range(len(lst)):
    if lst[i] != 0:
        if point != i:
            temp = lst[point]
            lst[point] = lst[i]
            lst[i] = temp
        point += 1
for i in range(len(lst)):
    print(lst[i], end=" ")
