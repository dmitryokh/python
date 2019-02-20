minutes = int(input())
minutes = minutes % 1440
hours = minutes // 60
minutes = minutes % 60
print(hours, minutes)
