n = int(input())
if (n % 10 == 1) and (n != 11):
    print(n, "korova")
elif (5 > n % 10 > 1) and ((n > 14) or (n < 12)):
    print(n, "korovy")
else:
    print(n, "korov")
