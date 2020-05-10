r= input("Input your revenue - ")
c= input("Input your costs - ")
p = int(r) - int(c)
if p > int(c):
    print ("Good job! Your profit",(p/int(r))*100)
    e=input("Input the number of employees - ")
    print(p / int(e), "for employee")
elif p < int(c):
    print("Bad job!")
