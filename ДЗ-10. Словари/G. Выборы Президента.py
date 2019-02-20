input = open('input.txt', 'r')
candidate = input.readline()
election = {}
maxvotes = 0
max2votes = 0
countvotes = 0
vote = {}
while candidate != "":
    if "\n" in candidate:
        candidate = candidate[:len(candidate)-1]
    if candidate in election:
        election[candidate] += 1
        vote[candidate] += 1
    else:
        election[candidate] = 1
        vote[candidate] = 1
    countvotes += 1
    candidate = input.readline()

for cand in vote:
    if vote[cand] > maxvotes:
        maxvotes = vote[cand]
        maxcand = cand
del vote[maxcand]
for cand in vote:
    if vote[cand] > max2votes:
        max2votes = vote[cand]
        max2cand = cand

if countvotes // maxvotes < 2:
    for name, votes in sorted(election.items()):
        if votes == maxvotes:
            print(name)
            break
elif maxvotes == max2votes:
    for name, votes in sorted(election.items()):
        if votes == maxvotes:
            print(name)
            candidate1 = name
            break
    for name, votes in sorted(election.items()):
        if votes == maxvotes and candidate1 != name:
            print(name)
            break
else:
    for name, votes in sorted(election.items()):
        if votes == maxvotes:
            print(name)
            break
    for name, votes in sorted(election.items()):
        if votes == max2votes:
            print(name)
            break
