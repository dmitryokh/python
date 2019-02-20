set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
lst = list(set1 & set2)
lst.sort()
for i in range(len(lst)):
    print(lst[i], end=" ")
