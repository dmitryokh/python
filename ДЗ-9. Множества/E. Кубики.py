n, m = map(int, input().split())
seta = set()
setb = set()
for i in range(n):
    x = int(input())
    seta.add(x)
for i in range(m):
    x = int(input())
    setb.add(x)
intersec = list(seta & setb)
intersec.sort()
lista = list(seta - setb)
lista.sort()
listb = list(setb - seta)
listb.sort()
print(len(intersec))
for i in range(len(intersec)):
    print(intersec[i], end=" ")
print()
print(len(lista))
for i in range(len(lista)):
    print(lista[i], end=" ")
print()
print(len(listb))
for i in range(len(listb)):
    print(listb[i], end=" ")
