input = open('input.txt', 'r', encoding='utf-8')
a = int(input.readline())
b = int(input.readline())
output = open('output.txt', 'w')
for i in range(a, b+1):
    d1 = i // 1000
    d2 = i // 100 % 10
    d3 = i // 10 % 10
    d4 = i % 10
    if (d1 == d2 == d3 and d1 != d4)\
            or (d1 == d2 == d4 and d2 != d3)\
            or (d1 == d3 == d4 and d1 != d2)\
            or (d2 == d3 == d4 and d1 != d2):
        output.write(str(i))
        output.write("\n")
