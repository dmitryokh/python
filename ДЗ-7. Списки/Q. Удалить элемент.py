lst = list(map(int, input().split()))
index = int(input())
for i in range(index + 1, len(lst)):
    lst[i-1] = lst[i]
lst.pop()
for i in range(len(lst)):
    print(lst[i], end=" ")
