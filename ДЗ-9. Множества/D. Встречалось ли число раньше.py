lst = list(map(int, input().split()))
set1 = set()
for i in range(len(lst)):
    if lst[i] in set1:
        print("YES")
    else:
        print("NO")
    set1.add(lst[i])
