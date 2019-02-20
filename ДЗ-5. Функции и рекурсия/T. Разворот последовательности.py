def back(a):
    if int(a) != 0:
        a = int(input())
        back(a)
        print(a)

a1 = int(input())
a = a1
back(a)
print(a1)
