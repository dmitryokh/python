input = open('input.txt', 'r')
text = input.readline()
count = 0
dic = set()
while text != "":
    text = text.split()
    for word in text:
        if word not in dic:
            dic.add(word)
            count += 1
    text = input.readline()
input.close()
print(count)
