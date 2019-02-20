def IsAscending(lst):
    count = 1
    i = 1
    while i < len(lst) and lst[i] > lst[i-1]:
        count += 1
        i += 1
    if count == len(lst):
        return("YES")
    else:
        return("NO")

lst = list(map(int, input().split()))
print(IsAscending(lst))
