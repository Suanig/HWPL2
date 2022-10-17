# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр (отсекаем минус, считаем все в плюс).

# float_num = input('input float number: ')
# # print(type(float_num))
# sum = 0
# for i in float_num:
#     if i != '.':
#         sum += int(i)
# print(sum)

# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

# n = int(input('input N: '))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
#     print(factorial, end=' ')

# 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# n = int(input('Enter number: ')) 

# def sequence(n):

#     return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
# print(sequence(n))
# print(round(sum(sequence(n))))

# Задание 4.1 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# import random

# def fill_list(n: int) -> list: 
#     new_list = [random.randint(-n, n)]
#     for i in range(1, n):
#         new_list.append(random.randint(-n, n))
#         i += 1
#     return new_list

# def writing_file(k: int, n: int):
#    with open('file2_4.txt', 'w') as position:
#        for i in range(k):
#            position.write(f'{random.randint(0, n-1)}\n')

# def print_position():
#    path = 'file2_4.txt'
#    position = open(path, 'r')
#    pos_element = []
#    for line in position:
#     pos_element.append(int(line))
#    print(f'Позиции элементов: {pos_element}')
#    position.close()
#    return pos_element

# def product_elements(user_list: list, k: int) -> int:
#    path = 'file2_4.txt'
#    position = open(path, 'r')
#    product = 1
#    for line in position:
#     product = product * user_list[int(line)]
#    position.close()
#    return product

# n = int(input('Количество элементов: N = '))
# new_list = fill_list(n)
# k = int(input('Количество множителей: k = '))
# writing_file(k, n)
# print(f'Заданный список: {new_list}')
# print_position()
# print(f'Произведение элементов на заданных позициях равно {product_elements(new_list, k)}')

# Задание 4.2 Реализуйте алгоритм перемешивания списка.

# list = ['Веселый пианист', 250, 3.14, 'True ']
# print(list) 
# import random
# random.shuffle(list)
# print('->', list) 