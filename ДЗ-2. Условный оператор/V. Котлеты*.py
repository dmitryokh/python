k = int(input())
m = int(input())
n = int(input())
n *= 2
rep = n // k
if n <= k:
    ans = m * 2
elif n % k == 0:
    ans = rep * m
else:
    ans = (rep + 1) * m
print(ans)
