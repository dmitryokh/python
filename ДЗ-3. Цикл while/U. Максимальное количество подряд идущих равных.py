a = int(input())
comp = a
count = 1
maxcount = 0
while a != 0:
    a = int(input())
    if count > maxcount:
        maxcount = count
    if a == comp:
        count += 1
    else:
        count = 1
        comp = a
print(maxcount)
