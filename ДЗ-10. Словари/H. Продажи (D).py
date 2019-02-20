input = open('input.txt', 'r')
text = input.readline()
sellslist = []
while text != "":
    text = text.split()
    name = text[0]
    thing = text[1]
    price = int(text[2])
    sellslist.append(list(join(name, thing, price)))
    text = input.readline()
print(sellslist)
for i in sellslist:
    for j in sellslist:
        if i[0] == j[0] and i[1] == j[1] and i != j:
            i[2] += j[2]
            sellslist.remove(j)
print(sellslist)
