def gcd(a, b):
    if a == 0:
        return(b)
    elif b == 0:
        return(a)
    else:
        if a >= b:
            return(gcd(b, a % b))
        else:
            return(gcd(a, b % a))

def reduceFraction(n, m):
    div = gcd(n, m)
    return (n // div, m // div)

n = int(input())
m = int(input())
print(reduceFraction(n, m)[0], reduceFraction(n, m)[1])
