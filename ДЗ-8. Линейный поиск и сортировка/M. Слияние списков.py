def merge(a, b):
    c = []
    ai = bi = 0
    for i in range(len(a) + len(b)):
        if ai == len(a):
            c.append(b[bi])
            bi += 1
        elif bi == len(b):
            c.append(a[ai])
            ai += 1
        elif a[ai] <= b[bi]:
            c.append(a[ai])
            ai += 1
        else:
            c.append(b[bi])
            bi += 1
    for i in range(len(c)):
        print(c[i], end=" ")

a = list(map(int, input().split()))
b = list(map(int, input().split()))
merge(a, b)
