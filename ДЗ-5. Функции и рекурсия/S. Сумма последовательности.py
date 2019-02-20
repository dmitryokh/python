def sum(a, s):
    if a == 0:
        return(s)
    else:
        s += a
        a = int(input())
        return(sum(a, s))

a = int(input())
s = 0
print(sum(a, s))
