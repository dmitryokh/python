lst = list(map(int, input().split()))
for i in range((len(lst) + 1) // 2):
    temp = lst[i]
    lst[i] = lst[len(lst) - i - 1]
    lst[len(lst) - i - 1] = temp
for i in range(len(lst)):
    print(lst[i], end=" ")
