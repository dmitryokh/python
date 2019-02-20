def IsPointInSquare(x, y):
    return (not ((abs(x) + abs(y)) // 1.00000000001))

x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print("YES")
else:
    print("NO")
