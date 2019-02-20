input = open('input.txt', 'r', encoding='utf-8')
data = input.readline()
countsch = [0] * 99
while data != "":
    data = data.split()
    school = int(data[2])
    countsch[school] += 1
    data = input.readline()
input.close()
maxsch = max(countsch)
bestsch = []
for i in range(len(countsch)):
    if countsch[i] == maxsch:
        bestsch.append(i)
bestsch.sort()
for i in range(len(bestsch)):
    print(bestsch[i], end=" ")
