import math

a = int(input())
summ = 0
sqs = 0
n = 0
while a != 0:
    summ += a
    sqs += a**2
    n += 1
    a = int(input())
s = summ / n
ans = (sqs - 2*summ*s + n*s*s) / (n-1)
print(math.sqrt(ans))
