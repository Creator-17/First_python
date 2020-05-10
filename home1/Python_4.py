n = int(input("Input you number: "))
value = 0
num = n
while num > 0:
    b = num % 10
    if b > value:
        value = b
        if value == 9:
            break
    num = num // 10
print (f"{value}")