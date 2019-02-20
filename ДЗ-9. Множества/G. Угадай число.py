input = open('input.txt', 'r')
n = int(input.readline())
numb = set()
for i in range(1, n+1):
    numb.add(i)
nmbrs = input.readline().split()
while nmbrs != ['HELP']:
    yesno = input.readline()
    numset = set(map(int, nmbrs))
    if "YES" in yesno:
        numb &= numset
    else:
        numb -= numset
    nmbrs = input.readline().split()

numblist = list(numb)
numblist.sort()
for i in numblist:
    print(i, end=" ")
