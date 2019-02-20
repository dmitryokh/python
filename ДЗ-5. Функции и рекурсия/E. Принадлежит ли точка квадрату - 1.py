def IsPointInSquare(x, y):
    return((not abs(x) // 1.0000000000001) and (not abs(y) // 1.0000000000001))

x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print("YES")
else:
    print("NO")
