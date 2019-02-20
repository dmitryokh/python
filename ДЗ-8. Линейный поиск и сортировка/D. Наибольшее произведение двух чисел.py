lst = list(map(int, input().split()))
if len(lst) > 3:
    maxm = max(lst)
    lst.remove(maxm)
    maxm2 = max(lst)
    lst.remove(maxm2)
    minm = min(lst)
    lst.remove(minm)
    minm2 = min(lst)
    lst.remove(minm2)
    if maxm * maxm2 > minm * minm2:
        print(maxm2, maxm)
    else:
        print(minm, minm2)
elif len(lst) == 3:
    mult1 = lst[0] * lst[1]
    mult2 = lst[0] * lst[2]
    mult3 = lst[1] * lst[2]
    if mult1 >= mult2 and mult1 >= mult3:
        print(min(lst[0], lst[1]), max(lst[0], lst[1]))
    elif mult3 >= mult2 and mult3 >= mult1:
        print(min(lst[1], lst[2]), max(lst[1], lst[2]))
    elif mult2 >= mult1 and mult2 >= mult3:
        print(min(lst[0], lst[2]), max(lst[0], lst[2]))
else:
    print(min(lst[0], lst[1]), max(lst[0], lst[1]))
