# # Задание 1
# Дана переменная, в которой хранится слово из латинских букв. Напишите код, который выводит на экран:

# среднюю букву, если число букв в слове нечетное;
# две средних буквы, если число букв четное.
# Примеры работы программы:

# word = 'test'
# Результат:
# es

# word = 'testing'
# Результат:
# t
#Решение==========================
# word = 'test'
# length = int(len(word))
# if length %2 == 0:
#     print(word[int((length/2)-1)],word[int((length/2)+1)])
# else:
#     print(word[int(length/2)])

## Задание 2
# Напишите программу, которая последовательно запрашивает у пользователя числа (по одному за раз) и после первого нуля выводит сумму всех ранее введенных чисел.
# Примеры работы программы:
# Введите число:
# 1
# Введите число:
# 4
# Введите число:
# 6
# Введите число:
# 0
# Результат:
# 11
# Введите число:
# 0
# Результат:
# 0
# Решение =========================================
# final_sum = 0
# input_digit = int(input('Введите число: '))
# while input_digit != 0:
#     final_sum = final_sum + input_digit
#     input_digit = int(input('Введите число: '))
# print('Сумма введеных чисел:', final_sum)

## Задание 3
# Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек.
# Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту и познакомим людей с одинаковыми индексами после сортировки!
# Но мы не будем никого знакомить, если кто-то может остаться без пары:

# Примеры работы программы:

# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
# Результат:

# Идеальные пары:
# Alex и Emma
# Arthur и Kate
# John и Kira
# Peter и Liza
# Richard и Trisha
# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
# Результат:
# Внимание, кто-то может остаться без пары!

# Решение ====================
# import copy
# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
# # boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
# # girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
# ind = 0
# if len(boys) != len(girls):
#     print('Кто-то может отстаться без пары')
# else:
#     for pair in boys:
#         boys_sort = copy.copy(sorted(boys))
#         girls_sort = copy.copy(sorted(girls))
#         print (boys_sort[ind], 'и', girls_sort[ind])
#         ind += 1

## Задание 4
# У нас есть список, содержащий информацию о среднедневной температуре в Фаренгейтах за произвольный период по странам (структура данных в примере). 
# Необходимо написать код, который рассчитает среднюю температуру за период в Цельсиях(!) для каждой страны.

# Пример работы программы:

# countries_temperature = [
# ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
# ['Germany', [57.2, 55.4, 59, 59, 53.6]],
# ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
# ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
# ]
# Результат:

# Средняя температура в странах:
# Thailand - 23.9 С
# Germany - 13.8 С
# Russia - 3.7 С
# Poland - 12.0 С

#Решение======================
countries_temperature = [['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
['Germany', [57.2, 55.4, 59, 59, 53.6]],
['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]]
s = 0
for avg_temp in countries_temperature:
    country_temp = countries_temperature[s]
    avg_temp = sum(country_temp[1]) / len(country_temp[1])
    print(country_temp[0], '-', "{:.1f}".format(float((avg_temp-32)*5/9)), 'C')
    s += 1