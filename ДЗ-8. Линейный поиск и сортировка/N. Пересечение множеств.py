def intersection(a, b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            c.append(a[i])
            i += 1
            j += 1
        elif a[i] > b[j]:
            j += 1
        else:
            i += 1
    for i in range(len(c)):
        print(c[i], end=" ")

a = list(map(int, input().split()))
b = list(map(int, input().split()))
intersection(a, b)
