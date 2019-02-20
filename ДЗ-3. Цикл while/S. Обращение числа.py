n = int(input())
rev = 0
while n > 0:
    rev *= 10
    dig = n % 10
    rev += dig
    n //= 10
print(rev)
