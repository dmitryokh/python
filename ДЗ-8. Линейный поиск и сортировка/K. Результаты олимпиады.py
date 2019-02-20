n = int(input())

class Olymp:
    name = ""
    points = 0

rezlist = []

def sortkey(pupil):
    return(-pupil.points)

for i in range(n):
    temp = input().split()
    pupil = Olymp()
    pupil.name = temp[0]
    pupil.points = int(temp[1])
    rezlist.append(pupil)

rezlist.sort(key = sortkey)

for pupil in rezlist:
    print(pupil.name)
