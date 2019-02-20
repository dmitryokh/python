n = int(input())
i = 1
count = 0
while i <= n:
    rev = 0
    stra = i
    while stra > 0:
        rev *= 10
        dig = stra % 10
        rev += dig
        stra //= 10
    if rev == i:
        count += 1
    i += 1
print(count)
