a = int(input())
b = int(input())
c = a // b
c = ((c + 2) // (c+1)) % 2
d = (c + 1) % 2
print(d * b + c * a)
