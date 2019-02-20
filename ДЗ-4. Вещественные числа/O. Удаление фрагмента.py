str = input()
pos1 = str.find("h")
pos2 = str.rfind("h")
str1 = str[0:pos1] + str[pos2 + 1:len(str)]
print(str1)
