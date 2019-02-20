newclass = list(map(int, input().split()))
Petya = int(input())
index = 0
for i in range(len(newclass)):
    if Petya > newclass[i]:
        print(i + 1)
        index = 1
        break
if index == 0:
    print(len(newclass) + 1)
