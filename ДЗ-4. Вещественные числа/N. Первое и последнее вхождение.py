str = input()
pos1 = -1
pos2 = -2
pos1 = str.find("f")
pos2 = str.rfind("f")
if pos1 == pos2 and pos1 != -1:
    print(pos1)
elif pos1 != -1 and pos2 != -2:
    print(pos1, pos2)
