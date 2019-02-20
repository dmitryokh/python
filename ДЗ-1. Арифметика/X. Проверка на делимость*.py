a = int(input())
b = int(input())
no = a % b
no = ((no + 2) // (no + 1)) % 2
yes = (no + 1) % 2
print(yes * "Yes", no * "No", sep='')

