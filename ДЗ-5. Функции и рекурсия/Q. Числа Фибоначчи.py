def phib(n):
    if n == 0:
        return("0")
    elif n == 1 or n == 2:
        return("1")
    else:
        return(int(phib(n-1)) + int(phib(n-2)))

n = int(input())
print(phib(n))
