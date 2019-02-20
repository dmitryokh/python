class Pupil:
    surname = ""
    name = ""
    points = 0


input = open('input.txt', 'r', encoding='utf-8')
data = input.readline()
pupilslist = []
while data != "":
    data = data.split()
    person = Pupil()
    person.surname = data[0]
    person.name = data[1]
    person.points = int(data[3])
    pupilslist.append(person)
    data = input.readline()


def sortkey(person):
    return(person.surname)


pupilslist.sort(key=sortkey)

for person in pupilslist:
    print(person.surname, person.name, person.points)
