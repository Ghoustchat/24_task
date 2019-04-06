n = int(input())
minDigit = n
while n > 0:
    digit =  n % 10
    if digit % 2 == 0:
        if digit < minDigit:
            minDigit = digit
    n = n // 10
if minDigit % 2 !=0:
    print("NO")
else:
    print(minDigit)