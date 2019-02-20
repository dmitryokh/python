sizecust = int(input())
sizeshop = list(map(int, input().split()))
sizeshop.sort()
i = 0
count = 0
begin = 0
for i in sizeshop:
    if i >= sizecust:
        count = 1
        begin = sizeshop.index(i)
        break

if len(sizeshop) > 0:
    for i in range(len(sizeshop)):
        if sizeshop[begin] + 3 <= sizeshop[i]:
            count += 1
            begin = i
    print(count)
elif sizeshop[0] >= sizecust:
    print("1")
else:
    print("0")
