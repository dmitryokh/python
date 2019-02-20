km = list(map(int, input().split()))
pr = list(map(int, input().split()))
km.sort()
pr.sort(reverse=True)
summ = 0
for i in range(len(pr)):
    summ += km[i] * pr[i]
print(summ)
