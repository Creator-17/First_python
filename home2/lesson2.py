# task 1 ----------------------------------------------------------------------------------------------------------------
first_list = [1, 0.1, "lost"]
first_list.append(True)
first_list.append([3, 2, 1])
for i, el in enumerate(first_list):
    print(type(first_list[i]), "-", el)

# task 2 ----------------------------------------------------------------------------------------------------------------
number_1 = int(input("Input number_1 - "))
number_2 = int(input("Input number_2 - "))
number_3 = int(input("Input number_3 - "))
number_4 = int(input("Input number_4 - "))
number_5 = int(input("Input number_5 - "))
second_list = [number_1, number_2, number_3, number_4, number_5]
b = 0
for i in range(1, int(len(second_list) / 2)):
    second_list[b], second_list[b + 1] = second_list[b + 1], second_list[b]
    b += 2
    print(second_list)  # как выводить только 2 вариант?

# task 3 ----------------------------------------------------------------------------------------------------------------
month = int(input("Input month - "))
dict = {12: 'Winter!', 1: 'Winter!', 2: 'Winter!', 3: 'Spring!', 4: 'Spring!', 5: 'Spring!', 6: 'Summer!', 7: 'Summer!',
        8: 'Summer!', 9: 'Autumn!', 10: 'Autumn!', 11: 'Autumn!'}
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

if 3 <= list[month] <= 5:
    print("Spring!")
    print(dict[month])
elif 6 <= list[month] <= 8:
    print("Summer!")
    print(dict[month])
elif 9 <= list[month] <= 11:
    print("Autumn!")
    print(dict[month])
elif 12 <= list[month] <= 2:
    print("Winter!")
    print(dict[month])

# task 4 ----------------------------------------------------------------------------------------------------------------
words = input("Input words - ")
words_2 = words.split()
print(words_2)

for i, el in enumerate(words_2, 1):
    print(i, el[:10])

# task 5 ----------------------------------------------------------------------------------------------------------------
rate = [7, 5, 4, 2]
p_rate = int(input("Input rate - "))
n = -1
while p_rate > 0:
    if p_rate < rate[n]:
        rate.append(p_rate)
        break
    elif p_rate > rate[0]:
        rate.insert(0, p_rate)
        break
    elif p_rate == rate[n]:
        rate.insert(n, p_rate)
        break
    elif p_rate < rate[0]:
        n -= 1
print(rate)

# task 6 ----------------------------------------------------------------------------------------------------------------
count = int(input('Введите количество товаров которые хотите приобрести: '))
i = count
b = 1
с = 0
products_name = []
products_price = []
products_count_p = []
products_unit = []
catalog = []
while b <= i:
    name = input("Наименование - ")
    price = int(input("Цена - "))
    count_p = int(input("Количество - "))
    unit = input("Еденица - ")
    products_name.append(name)
    products_price.append(price)
    products_count_p.append(count_p)
    products_unit.append(unit)
    catalog.append((b, {f"название": products_name[с], "цена": products_price[с], "количество": products_count_p[с],
                        "ед": products_unit[с]}))
    b += 1
    с += 1
    print(catalog)
for i in catalog:
    print(i)
    for el in i[1].values():
        print(el)
