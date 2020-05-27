# task 1 --------------------------------------------------------------------------------
my_txt = open('test.txt', 'w', encoding="utf-8")
text = input('Введите текст\n')
while text:
    my_txt.writelines(f'{text}\n')
    text = input('Введите текст\n')
    if not text:
        break

my_txt.close()

my_txt = open('test.txt', 'r')
content = my_txt.readlines()
print(content)
my_txt.close()

# task 2 --------------------------------------------------------------------------------
my_file = open('test.txt', 'r', encoding="utf-8")
content = my_file.read()
print(f'Содержимое файла: \n{content}')
my_file = open('test.txt', 'r', encoding="utf-8")
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
for i in range(len(content)):
    print(
        f'Количетво символов {i + 1} - ой строки {len(content[i]) - 1}')
my_file.close()

# task 3 --------------------------------------------------------------------------------
my_file = open('text_3.txt', 'r', encoding="utf-8")
sal = []
poor = []
my_list = my_file.read().split('\n')
for i in my_list:
    i = i.split()
    if float(i[1]) < 20000:
        poor.append(i[0])
    sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(float, sal)) / len(sal)}')

# task 4 --------------------------------------------------------------------------------
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('text_4.txt', 'r', encoding="utf-8") as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('file_4_new.txt', 'w', encoding="utf-8") as file_obj_2:
    file_obj_2.writelines(new_file)


# task 5 --------------------------------------------------------------------------------

def fun():
    try:
        with open('file_5.txt', 'w+', encoding="utf-8") as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_num = line.split()
            print(sum(map(int, my_num)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')


fun()

# task 6 --------------------------------------------------------------------------------

my_file = open('text_6.txt', 'r', encoding="utf-8")
content = my_file.readlines()
subj = {}
print(content)
for i in content:
    subject, lecture, practice, lab = i.split()
    print(i.split())
# subj[subject] = int(lecture[0:2]) + int(practice[0:2]) + int(lab[0:2])
#     print(f'Общее   часов по предмету - \n {subj}')

# task 7 --------------------------------------------------------------------------------
import json

profit = {}
pr = {}
prof = 0
prof_avg = 0
i = 0
with open('text_7.txt', 'r', encoding="utf-8") as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_avg = prof / i
        print(f'Прибыль средняя - {prof_avg:.2f}')
    else:
        print(f'Все работают в убыток')
    pr = {'средняя прибыль': round(prof_avg)}
    profit.update(pr)
    print(f'Результат каждой компании - {profit}')
with open('text_77.json', 'w') as write_js:
    json.dump(profit, write_js)

