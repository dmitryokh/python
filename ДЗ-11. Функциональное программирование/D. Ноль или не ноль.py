import sys
print(not bool(min
               (map
                (lambda x: abs(x), list
                (map
                 (int, sys.stdin.read().strip("\n").split()))))))
