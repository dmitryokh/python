str = input()
space = str.find(" ")
str1 = str[space + 1:len(str)] + " " + str[0:space]
print(str1)
