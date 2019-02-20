def c(n, k):
    if k == n:
        return("1")
    elif k == 0:
        return("1")
    elif k == 1:
        return(n)
    else:
        return (int(c(n-1, k-1)) + int(c(n-1, k)))

n = int(input())
k = int(input())
print(c(n, k))
