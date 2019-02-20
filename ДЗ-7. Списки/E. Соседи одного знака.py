lst = list(map(int, input().split()))
for i in range(1, len(lst)):
    if lst[i] * lst[i-1] > 0:
        print(lst[i-1], lst[i], end=" ")
        break
