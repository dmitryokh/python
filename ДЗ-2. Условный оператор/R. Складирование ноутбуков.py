a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

an1 = a1 // a2
an2 = b1 // b2
an3 = c1 // c2

e1 = an1 * an2 * an3

an1 = a1 // b2
an2 = b1 // a2
an3 = c1 // c2

e2 = an1 * an2 * an3

an1 = a1 // a2
an2 = b1 // c2
an3 = c1 // b2

e3 = an1 * an2 * an3

an1 = a1 // c2
an2 = b1 // a2
an3 = c1 // b2

e4 = an1 * an2 * an3

an1 = a1 // c2
an2 = b1 // b2
an3 = c1 // a2

e5 = an1 * an2 * an3

an1 = a1 // b2
an2 = b1 // c2
an3 = c1 // a2

e6 = an1 * an2 * an3

if (e1 >= e2) and (e1 >= e3) and (e1 >= e4) and (e1 >= e5) and (e1 >= e6):
    print(e1)
elif (e2 >= e1) and (e2 >= e3) and (e2 >= e4) and (e2 >= e5) and (e2 >= e6):
    print(e2)
elif (e3 >= e1) and (e3 >= e2) and (e3 >= e4) and (e3 >= e5) and (e3 >= e6):
    print(e3)
elif (e4 >= e1) and (e4 >= e3) and (e4 >= e2) and (e4 >= e5) and (e4 >= e6):
    print(e4)
elif (e5 >= e1) and (e5 >= e3) and (e5 >= e4) and (e5 >= e2) and (e5 >= e6):
    print(e5)
else:
    print(e6)
