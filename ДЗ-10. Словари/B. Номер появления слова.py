input = open('input.txt', 'r')
text = input.readline()
words = {}
while text != "":
    text = text.split()
    for word in text:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
        print(words[word] - 1, end=" ")
    text = input.readline()
input.close()
