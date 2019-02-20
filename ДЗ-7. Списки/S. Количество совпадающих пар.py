lst = list(map(int, input().split()))
count = 0
for i in range(len(lst)):
    count += lst.count(lst[i]) - 1
print(count // 2)
