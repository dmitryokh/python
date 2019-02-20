a = int(input())
b = int(input())
amounta = a // b
amounta = ((amounta + 2) // (amounta + 1)) % 2
amountb = (amounta + 1) % 2
print(amountb * b + amounta * a)

