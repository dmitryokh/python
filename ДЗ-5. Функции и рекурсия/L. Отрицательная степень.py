def power(a, n, pow):
    while n > 0:
        pow *= a
        n -= 1
    while n < 0:
        pow /= a
        n += 1
    return(pow)

a = float(input())
n = int(input())
pow = 1
print(power(a, n, pow))
