h = int(input())
m = int(input())
s = int(input())
total = s + m * 60 + h * 3600
print(total / 86400 * 720)
