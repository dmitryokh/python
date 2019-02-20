from math import floor

p = int(input())
x = int(input())
y = int(input())
k = int(input())
i = 1
while i <= k:
    money = (x * 100 + y) * (p + 100) / 100
    x = int(money // 100)
    y = floor(money % 100)
    i += 1
print(x, y)
