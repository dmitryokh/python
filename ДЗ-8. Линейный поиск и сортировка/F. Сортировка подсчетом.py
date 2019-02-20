def countsort(lst):
    count = [0] * 101
    key = 0
    for i in range(len(lst)):
        count[lst[i]] += 1
    for i in range(len(count)):
        for j in range(key, key + count[i]):
            lst[j] = i
        key += count[i]

lst = list(map(int, input().split()))
countsort(lst)
for i in range(len(lst)):
    print(lst[i], end=" ")
