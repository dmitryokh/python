lst = list(map(int, input().split()))
for i in range(len(lst) - 1, -1, -1):
    print(lst[i], end=" ")
