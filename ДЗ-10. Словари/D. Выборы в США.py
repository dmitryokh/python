input = open('input.txt', 'r')
candidate = input.readline()
election = {}
while candidate != "":
    candidate = candidate.split()
    name = candidate[0]
    points = int(candidate[1])
    if name in election:
        election[name] += points
    else:
        election[name] = points
    candidate = input.readline()
input.close()
for name, points in sorted(election.items()):
    print(name, points)
