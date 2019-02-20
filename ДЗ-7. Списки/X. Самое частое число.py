lst = list(map(int, input().split()))
amount = []
number = []
for i in range(len(lst)):
    if lst[i] in number:
        amount[number.index(lst[i])] += 1
    else:
        number.append(lst[i])
        amount.append(1)
print(number[amount.index(max(amount))])
