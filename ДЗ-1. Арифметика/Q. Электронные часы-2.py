seconds = int(input())
seconds = seconds % 86400
hours = seconds // 3600
minutes = seconds // 60 - hours * 60
seconds = seconds % 60
min1 = minutes // 10
min2 = minutes % 10
sec1 = seconds // 10
sec2 = seconds % 10
print(hours, ":", min1, min2, ":", sec1, sec2, sep="")
