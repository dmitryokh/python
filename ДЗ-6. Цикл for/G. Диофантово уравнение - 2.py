a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
count = 0
for x in range(0, 1001):
    if (a * x ** 3 + b * x ** 2 + c * x + d) == 0 and x - e != 0:
        count += 1
print(count)
