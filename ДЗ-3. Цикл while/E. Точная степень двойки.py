n = int(input())
i = 1
k = 1
while i <= n:
    if i == k:
        k *= 2
    i += 1
k = k // 2
if n == k:
    print("YES")
else:
    print("NO")
