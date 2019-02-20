a = int(input())
count = 1
maxcount = 1
sign = 0
numb = 1
while a != 0:

    if numb == 1:
        pass
    elif numb == 2 and a != aprev:
        count += 1
    elif sign == -1 and a < aprev:
        count += 1
    elif sign == 1 and a > aprev:
        count += 1
    elif a == aprev:
        count = 1
    else:
        count = 2

    if numb == 1:
        pass
    elif a > aprev:
        sign = 1
    elif a < aprev:
        sign = -1
    else:
        sign = 0

    if count > maxcount:
        maxcount = count

    aprev = a
    a = int(input())
    numb += 1

print(maxcount)
