n = int(input())
n1 = n % 10
n2 = (n // 10) % 10
n3 = (n // 100) % 10
n4 = (n // 1000) % 10
s1 = n1 * 10 + n2
s2 = n4 * 10 + n3
print(s2 - s1 + 1)
