input = open('input.txt', 'r')
n = int(input.readline())
languageset = set()
for i in range(n):
    m = int(input.readline())
    pupil = set()
    for j in range(m):
        language = input.readline()
        pupil.add(language)
        if "\n" in language:
            language = language[:len(language)-1]
        languageset.add(language)
    if i == 0:
        wellknown = set()
        for j in pupil:
            if "\n" in j:
                wellknown.add(j[:len(j) - 1])
            else:
                wellknown.add(j)
    else:
        for j in pupil:
            if "\n" in j:
                pupil.add(j[:len(j)-1])
                pupil.remove(j)
        wellknown &= pupil

print(len(wellknown))
for i in wellknown:
    print(i)
print(len(languageset))
for i in languageset:
    print(i)
