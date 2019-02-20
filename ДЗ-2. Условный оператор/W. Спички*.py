l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())

len1 = r1 - r1
len2 = r2 - l2
len3 = r3 - l3

cross12 = cross13 = cross23 = 0
if (l2 <= l1 <= r2) or (l1 <= r2 <= r1) or (l1 <= l2 <= r1):
    cross12 = 1
if (l1 <= l3 <= r1) or (l3 <= r1 <= r3) or (l3 <= l1 <= r3):
    cross13 = 1
if (l2 <= l3 <= r2) or (l3 <= r2 <= r3) or (l3 <= l2 <= r3):
    cross23 = 1

if cross12 + cross23 + cross13 >= 2:
    print("0")
elif cross12:
    print("1")
elif (l2 < l3) and (l3 - r2 <= len1):
    print("1")
elif (l3 < l2) and (l2 - r3 <= len1):
    print("1")
elif cross13:
    print("2")
elif (l1 < l3) and (l3 - r1 <= len2):
    print("2")
elif (l3 < l1) and (l1 - r3 <= len2):
    print("2")
elif cross23:
    print("3")
elif (l1 < l2) and (l2 - r1 <= len3):
    print("3")
elif (l2 < l1) and (l1 - r2 <= len3):
    print("3")
else:
    print("-1")
