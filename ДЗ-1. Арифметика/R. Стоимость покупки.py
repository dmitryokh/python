rub = int(input())
kop = int(input())
am = int(input())
kop *= am
rub *= am
rub += (kop // 100)
kop = kop % 100
print (rub, kop)
