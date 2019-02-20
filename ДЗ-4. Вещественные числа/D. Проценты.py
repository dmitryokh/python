from math import floor

p = int(input())
x = int(input())
y = int(input())
money = (x * 100 + y) * (p + 100) / 100
x = int(money // 100)
y = floor(money % 100)
print(x, y)
