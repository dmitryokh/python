def wit(witness):
    a = 0
    for i in list1:
        if set(list(i)) <= set(list(witness)):
            a = a + 1
    return a

list1 = []
list2 = []
m = int(input())
for i in range(m):
    temp = input()
    list1.append(temp)
n = int(input())
for i in range(n):
    temp = input()
    list2.append(temp)
    numb = wit(max(list2, key=wit))
for i in list2:
    if wit(i) == numb:
        print(i)
