n = int(input())
dict = {}
for i in range(n):
    data = list(input().split())
    for j in range(1, len(data)):
        dict[data[j]] =  data[0]
k = int(input())
for j in range(k):
    city = input()
    print(dict[city])
