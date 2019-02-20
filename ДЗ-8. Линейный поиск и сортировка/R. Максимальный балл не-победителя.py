input = open('input.txt', 'r', encoding='utf-8')
data = input.readline()
class9 = set()
class10 = set()
class11 = set()
max9 = max10 = max11 = 0
while data != "":
    data = data.split()
    clas = int(data[2])
    points = int(data[3])
    if clas == 9:
        class9.add(points)
        if points > max9:
            max9 = points
    elif clas == 10:
        class10.add(points)
        if points > max10:
            max10 = points
    elif clas == 11:
        class11.add(points)
        if points > max11:
            max11 = points
    data = input.readline()
class9.remove(max9)
class10.remove(max10)
class11.remove(max11)
print(max(class9), max(class10), max(class11))
