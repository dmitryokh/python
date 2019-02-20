n = int(input())
i = 1
k = 1
while i <= n:
    if i == k:
        print(k, " ", sep="", end="")
        k *= 2
    i += 1
