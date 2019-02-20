input = open('input.txt', 'r')
text = input.readline()
wordcount = {}
while text != "":
    text = text.split()
    for word in text:
        if word in wordcount:
            wordcount[word] -= 1
        else:
            wordcount[word] = -1
    text = input.readline()
wordprint = []
for word, amount in sorted(wordcount.items()):
    mytuple = (amount, word)
    wordprint.append(mytuple)
wordprint.sort()
for amount, word in (wordprint):
    print(word)
