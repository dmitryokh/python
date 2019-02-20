def sum(a, b):
    if b == 0:
        return(a)
    else:
        return(sum(a, b-1) + 1)

a = int(input())
b = int(input())
if a >= b:
    print(sum(a, b))
else:
    print(sum(b, a))
