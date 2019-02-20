a1, a2, b1, b2 = map(int, input().split())
if a1 > a2:
    a1, a2 = a2, a1
if b1 > b2:
    b1, b2 = b2, b1
stops = [0] * 101
for i in range(a1, a2 + 1):
    stops[i] += 1
for i in range(b1, b2 + 1):
    stops[i] += 1
count = 0
for i in stops:
    if i == 2:
        count += 1
print(count)
