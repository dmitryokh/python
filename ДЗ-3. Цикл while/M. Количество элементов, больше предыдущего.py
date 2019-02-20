a = int(input())
aprev = a
a = int(input())
count = 0
while a != 0:
    if a > aprev:
        count += 1
    aprev = a
    a = int(input())
print(count)
