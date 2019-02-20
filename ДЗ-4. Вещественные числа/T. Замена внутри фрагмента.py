str = input()
str = str.replace("h", "H")
pos1 = str.find("H")
pos2 = str.rfind("H")
str1 = str[0:pos1] + "h" + str[pos1 + 1:pos2] + "h" + str[pos2 + 1:len(str)]
print(str1)
