# ; Домашнее задание к лекции "Основы Python"
# ; Задание 1
# ; Даны 2 переменных, в которых хранятся строки произвольной длины: phrase_1 и phrase_2.
# ; Напишите код, который проверяет какая из этих строк длиннее.  

# ; Примеры работы программы:
# ; 1.

# phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
# phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'

# ; Результат:
# ; Фраза 1 длиннее фразы 2 2.

# phrase_1 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
# phrase_2 = 'Насколько проще было бы писать программы, если бы не заказчики'
# ; Результат:
# ; Фраза 2 длиннее фразы 1 3.

# phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
# phrase_2 = 'Насколько проще было бы писать программы, если бы не заказчики'
# ; Результат:
# ; Фразы равной длины """

# Решение==================================================================
# phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
# phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
# if phrase_1<phrase_2:
#     print('Фраза 1 короче Фразы 2')
# elif phrase_1 == phrase_2:
#     print('Фразы равной длины')
# else:
#     print('Фраза 1 длиннее Фразы 2')
    
    
# ; Задание 2
# ; Дана переменная, в которой хранится число (год). Необходимо написать программу, которая выведет, является ли данный год високосным или обычным.

# ; Пример работы программы: 1.

# ; year = 2020
# ; Результат:
# ; Високосный год

# ; year = 2019
# ; Результат:
# ; Обычный год

#Решение======================
# year = int(input("Введите интересубщий год: "))
# if year % 4 == 0:
#     print (year, '- високосный год')
# else:
#     print (year, '- обычный год')

# ; Задание 3
# ; Необходимо написать программу, которая будет запрашивать у пользователя месяц и дату рождения и выводить соответствующий знак зодиака.

# ; Пример работы программы:
# ; 1.

# ; Введите день:
# ; 30

# ; Введите месяц:
# ; Август
# ; Результат:
# ; Ваш знак зодиака: Дева

# ; Введите день:
# ; 29

# ; Введите месяц:
# ; Октябрь
# ; Результат:
# ; Ваш знак зодиака: Скорпион
#Решение=====================
# month = int(input('Введите месяц интересуемого знака (от 1 до 12): '))
# day = int(input('Введите день рождения (от 1 до 31): '))
# if month == 3 and day >= 21 or month == 4 and day <= 20:
#     print ('Знак зодиака - Овен')
# elif month == 4 and day >= 21 or month == 5 and day <= 21:
#     print ('Знак зодиака - Телец')
# elif month == 5 and day >= 22 or month == 6 and day <= 21:
#     print ('Знак зодиака - Близнецы')
# elif month == 6 and day >= 22 or month == 7 and day <= 22:
#     print ('Знак зодиака - Рак')
# elif month == 7 and day >= 23 or month == 8 and day <= 21:
#     print ('Знак зодиака - Лев')
# elif month == 8 and day >= 22 or month == 9 and day <= 23:
#     print ('Знак зодиака - Дева')
# elif month == 9 and day >= 24 or month == 10 and day <= 23:
#     print ('Знак зодиака - Весы')
# elif month == 10 and day >= 24 or month == 11 and day <= 22:
#     print ('Знак зодиака - Скорпион')
# elif month == 11 and day >= 23 or month == 12 and day <= 22:
#     print ('Знак зодиака - Стрелец')
# elif month == 12 and day >= 23 or month == 1 and day <= 20:
#     print ('Знак зрдиака - Козерог')
# elif month == 1 and day >= 21 or month == 2 and day <= 19:
#     print ('Знак зрдиака - Водолей')
# elif month == 2 and day >= 20 or month == 3 and day <= 20:
#     print ('Знак зрдиака - Рыбы')
# else:
#     if month > 12 or month < 1 or day > 31 or day < 1:
#         print ('Некорректная дата')

# ; Задание 4
# ; Вам нужно написать программу для подбора упаковок по размерам товара. Размеры (ширина, длина, высота) хранятся в переменных (в сантиметрах):

# ; Используйте следующие правила:

# ; если каждое из трех измерений менее или равно 15 сантиметрам, то выведите на экран "Коробка №1";
# ; если хотя бы одно из измерений больше 2 метров, то выводите "Упаковка для лыж";
# ; если хотя бы одно из измерений больше 15 сантиметров, но менее 50 сантиметров, то выводите "Коробка №2";
# ; во всех остальных случаях выводите "Коробка №3".
# ; Пример работы программы:
# ; 1.

# ; width = 15
# ; length = 55
# ; height = 15
# ; Результат:
# ; Коробка №3

# ; width = 45
# ; length = 205
# ; height = 45
# ; Результат:
# ; Упаковка для лыж
# Решение===================================
# width = int(input('Введите ширину в см (больше нуля): '))
# length = int(input('Введите длину в см (больше нуля): '))
# height = int(input('Введите высоту в см (больше нуля): '))
# if width <= 0 or length <= 0 or height <=0:
#     print('Неправильный размер')
# elif width <= 15 and width > 0 and length <= 15 and length > 0 and height <=15 and height > 0:
#     print('Коробка №1')
# elif (width > 15 and width < 50) or (length > 15 and length < 50) or (height > 15 and height < 50):
#     print('Коробка №2')
# elif width > 200 or length > 200 or height > 200:
#     print('Коробка для лыж')
# else:
#     print('Коробка №3')
# ; Задание 5 (необязательное)
# ; Дана переменная, в которой хранится шестизначное число (номер проездного билета). Напишите программу, которая будет определять,
# является ли данный билет "счастливым". Билет считается счастливым, 
# если сумма первых трех цифр совпадает с суммой последних трех цифр номера.

# ; Примеры работы программы:

# ; number = 123456
# ; Результат:
# ; Несчастливый билет

# ; number = 123321
# ; Результат:
# ; Счастливый билет
#Решение==============================
# number = str(input('Введите число больше нуля: '))
# if len(number) != 6:
#     print('Неверное число')
# else:
#     a = int(number[0])
#     b = int(number[1])
#     c = int(number[2])
#     d = int(number[3])
#     e = int(number[4])
#     f = int(number[5])
#     print(a,b,c,d,e,f)
#     if int(a+b+c) == int(d+e+f):
#         print('У вас счастливый билет')
#     else:
#         print('У вас НЕ счастливый билет')


# ; Задание 6 (необязательное)
# ; Напишите программу, которая сможет вычислять площади трех фигур (круг, треугольник и прямоугольник).
# Тип фигуры запрашиваем через пользовательский ввод, после чего делаем запрос характеристик фигуры:

# ; если пользователь выбрал круг, запрашиваем его радиус,
# ; если треугольник – длины трех его сторон;
# ; если прямоугольник – длины двух его сторон.
# ; Пример работы программы:
# ; 1.

# ; Введите тип фигуры:
# ; Круг

# ; Введите радиус круга:
# ; 10
# ; Результат:
# ; Площадь круга: 314.16

# ; Введите тип фигуры:
# ; Треугольник

# ; Введите длину стороны A:
# ; 2

# ; Введите длину стороны B:
# ; 2

# ; Введите длину стороны C:
# ; 3
# ; Результат:
# ; Площадь треугольника: 1.98        
#Решение=====================
import math
type_of_figure = int(input('Введите тип фигуры, 1 - Круг, 2 - Треугольник, 3 - Прямоугольник '))
if type_of_figure == 1:
    radius = int(input('Введите радиус:'))
    circule_square = 2 * 3.14 * radius
    print('Радиус круга = ' , round(circule_square,2))
elif type_of_figure == 2:
    width = int(input('Введите длину стороны 1:'))
    length = int(input('Введите длину стороны 2:'))
    height = int(input('Введите длину стороны 3:'))
    half_perimeter = (width + length + height) / 2
    triangle_square = math.sqrt(half_perimeter * (half_perimeter - width) * (half_perimeter - length) * (half_perimeter - height))
    print('Площадь теругольника = ', round(triangle_square,2))
elif type_of_figure == 3:
    width_sq = int(input('Введите ширину:'))
    height_sq = int(input('Введите длину:'))
    square = (width_sq * height_sq) / 2
    print('Площадь треуголтника = ', round(square,2))
else:
    print('Указан неверный тип фигуры')