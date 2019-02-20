aprev = int(input())
a = int(input())
count = 0
if a != 0:
    anext = int(input())
else:
    anext = 0
while anext != 0:
    if a > aprev and a > anext:
        count += 1
    aprev = a
    a = anext
    anext = int(input())
print(count)
