def ishigher2xplus2(x, y):
    return (y > 2 * x + 2)


def ishigherminusx(x, y):
    return (y > x * (-1))


def isoutscircle(x, y):
    return ((x+1) ** 2 + (y-1) ** 2 > 4)


def iseq2xplus2(x, y):
    return (y == 2 * x + 2)


def iseqminusx(x, y):
    return(y == x * (-1))


def ifeqcircle(x, y):
    return((x+1) ** 2 + (y-1) ** 2 == 4)


def ispointarearea(x, y):
    a = ishigher2xplus2(x, y)
    b = ishigherminusx(x, y)
    c = isoutscircle(x, y)
    d = iseq2xplus2(x, y)
    e = iseqminusx(x, y)
    f = ifeqcircle(x, y)
    cond1 = ((a or d) and (b or e) and (not c or f))
    cond2 = ((not a or d) and (not b or e) and (c or f))
    return(cond1 or cond2)

x = float(input())
y = float(input())
if ispointarearea(x, y):
    print("YES")
else:
    print("NO")
