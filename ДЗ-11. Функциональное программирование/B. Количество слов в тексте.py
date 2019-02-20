import sys
print(len(set(list(sys.stdin.read().replace("\n", " ").split(" ")))) - 1)
