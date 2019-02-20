n = int(input())
minutes = n * 45 + ((n) // 2) * 5 + ((n - 1) // 2) * 15
hours = minutes // 60
minutes = minutes % 60
print(9 + hours, minutes)
