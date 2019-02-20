a = int(input())
sign = 0
numb = 1
dist = 0
mindist = 1000000000000
countmax = 0
while a != 0:

    if numb == 1:
        pass
    elif sign == 1 and a < aprev:
        countmax += 1
        if countmax != 1:
            dist = numb - numbmax
            if dist < mindist:
                mindist = dist
        numbmax = numb

    if numb == 1:
        pass
    elif a > aprev:
        sign = 1
    elif a < aprev:
        sign = -1
    else:
        sign = 0

    aprev = a
    a = int(input())
    numb += 1

if countmax < 2:
    print("0")
else:
    print(mindist)
