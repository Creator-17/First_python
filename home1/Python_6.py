a = int(input("Input your result - "))
b = int(input("Input your finish result - "))
c= 1

while a < b:
    a = (a * 0.1) + a
    c = c+1
print(c)
