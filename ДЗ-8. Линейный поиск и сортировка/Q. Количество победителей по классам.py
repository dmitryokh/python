input = open('input.txt', 'r', encoding='utf-8')
data = input.readline()
count9 = count10 = count11 = max9 = max10 = max11 = 0
while data != "":
    data = data.split()
    clas = int(data[2])
    points = int(data[3])
    if clas == 9:
        if points > max9:
            max9 = points
            count9 = 0
        if points == max9:
            count9 += 1
    elif clas == 10:
        if points > max10:
            max10 = points
            count10 = 0
        if points == max10:
            count10 += 1
    elif clas == 11:
        if points > max11:
            max11 = points
            count11 = 0
        if points == max11:
            count11 += 1
    data = input.readline()
print(count9, count10, count11)

