n = int(input())
keyboard = list(map(int, input().split()))
k = int(input())
press = list(map(int, input().split()))
for i in range(k):
    keyboard[press[i] - 1] -= 1
for i in range(len(keyboard)):
    if keyboard[i] < 0:
        print("YES")
    else:
        print("NO")
