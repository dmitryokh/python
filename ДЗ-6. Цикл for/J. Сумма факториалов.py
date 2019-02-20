def fact(n):
    if n == 1:
        return(n)
    else:
        return(n * fact(n-1))

n = int(input())
sum = 0
for i in range(1, n+1):
    sum += fact(i)
print(sum)
