x = []
y = []
index = 0
for i in range(8):
    temp1, temp2 = map(int, input().split())
    x.append(temp1)
    y.append(temp2)
for i in range(8):
    if x.count(x[i]) != 1 or y.count(y[i]) != 1:
        index = 1
        break
    for j in range(8):
        if x[i] + y[i] == x[j] + y[j] and i != j:
            index = 1
            break
if index == 1:
    print("YES")
else:
    print("NO")
