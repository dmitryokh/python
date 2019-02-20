a = int(input())
b = int(input())
c = int(input())
even = 0
odd = 0
if a % 2 == 0:
    even += 1
else:
    odd += 1
if b % 2 == 0:
    even += 1
else:
    odd += 1
if c % 2 == 0:
    even += 1
else:
    odd += 1
if (even > 0) and (odd > 0):
    print("YES")
else:
    print("NO")
