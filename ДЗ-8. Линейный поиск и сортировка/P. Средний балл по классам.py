input = open('input.txt', 'r', encoding='utf-8')
data = input.readline()
count9 = count10 = count11 = sum9 = sum10 = sum11 = 0
while data != "":
    data = data.split()
    clas = int(data[2])
    points = int(data[3])
    if clas == 9:
        count9 += 1
        sum9 += points
    elif clas == 10:
        count10 += 1
        sum10 += points
    elif clas == 11:
        count11 += 1
        sum11 += points
    data = input.readline()
print(sum9 / count9, sum10 / count10, sum11 / count11)
