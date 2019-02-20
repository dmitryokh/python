tel = []
for i in range(4):
    tel.append(input())
for i in range(4):
    tel[i] = tel[i].replace("+7", "8")
    tel[i] = tel[i].replace("(", "")
    tel[i] = tel[i].replace(")", "")
    tel[i] = tel[i].replace("-", "")
    if len(tel[i]) == 7:
        tel[i] = "8495" + tel[i]
for i in range(1, 4):
    if tel[0] == tel[i]:
        print("YES")
    else:
        print("NO")
