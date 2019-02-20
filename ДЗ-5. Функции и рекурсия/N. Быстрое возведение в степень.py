def power1(a, n):
    if n == 0:
        return("1")
    elif n == 1:
        return(a)
    else:
        if n % 2 == 0:
            return(power1(a ** 2, n/2))
        else:
            return(power1(a, n - 1) * a)


def power2(a, n):
    if n == -1:
        return(1/a)
    else:
        if n % 2 == 0:
            return(power2(a ** 2, n/2))
        else:
            return(power2(a, n - 1) / a)


a = float(input())
n = int(input())
if a == 0:
    print("0")
elif n >= 0:
    print(power1(a, n))
else:
    print(power2(a, n))
