n = int(input())
s = 0
min_dif = 10001
for i in range(n):
    a, b, c = map(int, input().split())
    if a > b :
        t = a
        a = b
        b = t
    if b > c:
        t = b
        b = c
        c = t
        if a > b:
            t = a
            a = b
            b = t
    # до этого момента мы упорядочиваем числа по возрастанию, так удобнее с ними работать
    s += a # добавляем в сумму минимальное
    if b - a < min_dif and (b - a) % 5 != 0:
        min_dif = b - a
    if c - a < min_dif and (c - a) % 5 != 0:
        min_dif = c - a
    # тут мы считали минимальную разницу
if s % 5 == 0:
    if min_dif == 10001:
        s = 0
    else :
        s += min_dif
print(s)