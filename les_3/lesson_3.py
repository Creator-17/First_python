# task 1 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def my_fun(a_1, a_2):
    """Division.

   Params a_1 and a_2 from user without number null!
    """
    try:
        a_2 > 0
        a_3 = a_1 / a_2
        print(f"Result {a_3}")
    except ZeroDivisionError:
        print("Not number - null!!!")


my_fun(int(input("Input your number_1: ")), int(input("Input your number_2: ")))


# task 2 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def my_fun(name_f, date_f, city_f, email_f, tel_f):
    print(
        f"Hello, {name_f}! You were born in {date_f}. Your city - {city_f}. Your email - {email_f}, your tel.number - {tel_f}")


my_fun(name_f=input("Input your name: "), date_f=int(input("Input your year of bithday - ")),
       city_f=input("Input your city: "), email_f=input("Input your mail: "),
       tel_f=int(input("Input your telepfone: ")))


# task 3 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def my_fun(a, b, c):
    list = [a, b, c]
    list.remove(min(a, b, c))
    return sum(list)


print(my_fun(int(input("input your number -")), int(input("input your number -")), int(input("input your number -"))))


# task 4 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#p1
def my_fun(x, y):
    return 1 / x ** abs(y)


print(my_fun(int(input("input your number -")), int(input("input your negative number -"))))

#p2

def my_fun(x,y):
    res = x
    for i in range(abs(y) - 1)):
        res *= x
    return 1 / res # почему x = 0??

print(my_fun(x=(int(input("input your number -"))), y=(int(input("input your negative number -")))))

# task 5 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def my_fun():
    n = 0
    while True:
        numbers = input('Enter list of number or * to exit: ').split()
        for i in numbers:
            try:
                if i == '*':
                    print(f'Sum is {n}. Exit')
                    return
                else:
                    n += int(i)
            except ValueError:
                print('Enter number or *')
        print(f'Sum is {n}')

my_fun()

# task 6 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def my_fun(text):
    ls = []
    for i in range(len(text)):
        ls.append(text[i][0:1].title() + text[i][1:])
    return ls

print(my_fun(text=input('Input your message: ').split()))