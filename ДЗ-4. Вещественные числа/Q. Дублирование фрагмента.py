str = input()
pos1 = str.find("h")
pos2 = str.rfind("h")
str1 = str[0:pos1 + 1] + str[pos1+1:pos2] * 2 + str[pos2:len(str)]
print(str1)
