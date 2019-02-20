n = int(input())
sum = n % 10
n //= 10
sum += n % 10
n //= 10
sum += n
print (sum)
