lst = list(map(int, input().split()))
for i in range(1, len(lst) + ((len(lst) + 1) % 2), 2):
    temp = lst[i]
    lst[i] = lst[i-1]
    lst[i-1] = temp
for i in range(len(lst)):
    print(lst[i], end=" ")
