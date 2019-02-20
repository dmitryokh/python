str = input()
pos1 = str.find("f")
if pos1 == -1:
    print("-2")
else:
    pos2 = str.find("f", pos1 + 1)
    print(pos2)
