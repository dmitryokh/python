str = input()
i = 0
str1 = ""
while i < len(str):
    if i % 3 != 0:
        str1 += str[i]
    i += 1
print(str1)
