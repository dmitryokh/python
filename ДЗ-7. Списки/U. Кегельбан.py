n, k = map(int, input().split())
bowl = []
for i in range(n):
    bowl.append("I")
for i in range(k):
    l, r = map(int, input().split())
    for j in range(l-1, r):
        bowl[j] = "."
for i in range(n):
    print(bowl[i], end="")
