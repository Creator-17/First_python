# task 1 --------------------------------------------------------------------
from sys import argv

script_name, hours, sum, prem = argv

print("Имя скрипта: ", script_name)
print("Параметр 1 : ", hours)
print("Параметр 2 : ", sum)
print("Параметр 3 : ", prem)


def ras_zp():
    from sys import argv
    script_name, hours, sum, prem = argv
    pay = int(hours) * int(sum)
    return (f'Размер заработной платы составил:{pay + int(prem):.2f}')


print(ras_zp())

# task 2 --------------------------------------------------------------------
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
print(new_list)

# task 3 --------------------------------------------------------------------
new_list = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
print(new_list)

# task 4 --------------------------------------------------------------------
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [i for i in my_list if my_list.count(i) == 1]
print(new_list)

# task 5 --------------------------------------------------------------------
from functools import reduce

a = [i for i in range(100, 1001)]
sum_all = reduce(lambda x, y: x + y, a)
print(sum_all)

# task 6 --------------------------------------------------------------------
from itertools import count, cycle

a = []

for el in count(1):
    if el > 7:
        break
    else:
        a.append(el)
print(a)
c = 0
for el in cycle(a):
    if c > 10:
        break
    print(el)
    c += 1


# task 7 --------------------------------------------------------------------
from math import factorial
generator = (factorial(i) for i in range (5))
for el in generator:
    print(el)

def gen():
    for el in generator:
        yield el
    print (el)

for i in gen():
   print(i)


