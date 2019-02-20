n, k = map(int, input().split())
strikes = set()
a = [0] * n
b = [0] * n
for i in range(k):
    a[i], b[i] = map(int, input().split())
    while a <= n:
        if a % 7 != 0 and a % 7 != 6:
            strikes.add(a)
        a += b
print(len(strikes))
