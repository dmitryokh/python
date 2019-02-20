n = int(input())
sumtrue = 0
sumreal = 0
for i in range(1, n+1):
    sumtrue += i
for i in range(n-1):
    card = int(input())
    sumreal += card
print(sumtrue - sumreal)
