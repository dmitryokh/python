str = input()
i = 0
str1 = ""
while i < len(str) - 1:
    str1 += str[i]
    str1 += "*"
    i += 1
str1 += str[len(str) - 1]
print(str1)
