input = open('input.txt', 'r', encoding='utf-8')
data = input.readline()
max9 = max10 = max11 = 0
while data != "":
    data = data.split()
    clas = int(data[2])
    points = int(data[3])
    if clas == 9 and points > max9:
        max9 = points
    elif clas == 10 and points > max10:
        max10 = points
    elif clas == 11 and points > max11:
        max11 = points
    data = input.readline()
input.close()
print(max9, max10, max11)
