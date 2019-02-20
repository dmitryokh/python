input = open('input.txt', 'r')
text = input.readline()
wordcount = {}
maxword = 0
while text != "":
    text = text.split()
    for word in text:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
        if wordcount[word] > maxword:
            maxword = wordcount[word]
    text = input.readline()
for word in sorted(wordcount):
    if wordcount[word] == maxword:
        print(word)
        break
