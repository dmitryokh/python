a = int(input())
maxm = a
count = 0
while (a != 0):
    if a > maxm:
        maxm = a
        count = 1
    elif a == maxm:
        count += 1
    a = int(input())
print(count)
