n = int(input())
synon = {}
for i in range(n):
    word1, word2 = input().split()
    synon[word1] = word2
    synon[word2] = word1
word = input()
print(synon[word])
