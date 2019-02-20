import math

n = int(input())
i = 1
while i <= n:
    if (math.sqrt(i) // 1) == (math.sqrt(i) / 1):
        print(i, " ", sep="", end="")
    i += 1
