n = int(input())
i = 1
k = 1
deg = 0
while i <= n:
    if i == k:
        k *= 2
        deg += 1
    i += 1
k = k // 2
if (n == k):
    print(deg - 1)
else:
    print(deg)
    