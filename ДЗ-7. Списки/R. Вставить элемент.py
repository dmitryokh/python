lst = list(map(int, input().split()))
index, c = map(int, input(). split())
if index == len(lst):
    lst.append(c)
else:
    last = lst[len(lst) - 1]
    for i in range(len(lst) - 1, index, -1):
        lst[i] = lst[i - 1]
    lst[index] = c
    lst.append(last)
for i in range(len(lst)):
    print(lst[i], end=" ")
