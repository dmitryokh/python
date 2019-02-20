n = int(input())
x = float(input())
a = float(input())
i = 1
sum = a
while i <= n:
    a = float(input())
    sum = sum * x + a
    i += 1
print(sum)
