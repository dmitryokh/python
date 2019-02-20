from math import floor, ceil

x = float(input())
frac = x - int(x)
if frac < 0.5:
    print(floor(x))
else:
    print(ceil(x))
