maxm = int(input())
maxm2 = int(input())
if maxm2 > maxm:
    temp = maxm
    maxm = maxm2
    maxm2 = temp
a = int(input())
while a != 0:
    if a > maxm:
        maxm2 = maxm
        maxm = a
    elif a > maxm2:
        maxm2 = a
    a = int(input())
print(maxm2)
