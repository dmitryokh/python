lst = list(map(int, input().split()))
if len(lst) == 1:
    print(lst[0])
else:
    mnpos = lst.index(min(lst))
    mxpos = lst.index(max(lst))
    minm = min(lst)
    maxm = max(lst)
    lst.remove(minm)
    lst.remove(maxm)
    if mxpos < mnpos:
        lst.insert(mxpos, minm)
        lst.insert(mnpos, maxm)
    else:
        lst.insert(mnpos, maxm)
        lst.insert(mxpos, minm)
    for i in range(len(lst)):
        print(lst[i], end=" ")
