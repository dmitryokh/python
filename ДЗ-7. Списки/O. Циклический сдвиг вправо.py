lst = list(map(int, input().split()))
last = lst[len(lst) - 1]
for i in range(len(lst) - 1, 0, -1):
    lst[i] = lst[i-1]
lst[0] = last
for i in range(len(lst)):
    print(lst[i], end=" ")
