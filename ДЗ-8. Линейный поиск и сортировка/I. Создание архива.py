s, n = map(int, input().split())
lst = list()
summ = 0
for i in range(n):
    lst.append(int(input()))
lst.sort()
i = 0
while i < len(lst):
    if summ + lst[i] < s:
        summ += lst[i]
        i += 1
    else:
        break
print(i)
