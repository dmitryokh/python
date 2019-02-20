set1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
count = 0
for i in range(len(lst2)):
    if lst2[i] in set1:
        count += 1
print(count)
