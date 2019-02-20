word = input()
code = ""
one = {"b", "f", "p", "v"}
two = {"c", "g", "j", "k", "q", "s", "x", "z"}
three = {"d", "t"}
four = {"l"}
five = {"m", "n"}
six = {"r"}
nonee = {"a", "e", "h", "i", "o", "u", "w", "y"}
code += word[0]
for letter in range(1, len(word)):
    temp=""
    if word[letter] in one:
        temp = 1
    if word[letter] in two:
        temp = 2
    if word[letter] in three:
        temp = 3
    if word[letter] in four:
        temp = 4
    if word[letter] in five:
        temp = 5
    if word[letter] in six:
        temp = 6
    if code[-1] != str(temp):
        code += str(temp)


code = code[:4]
while len(code) < 4:
    code += "0"
print(code)
