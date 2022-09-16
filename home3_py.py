import random
import math
def create_list(n:int)->list:
    """генерирует список случайных чисел"""
    num_list=[random.randint(-20,20) for i in range(n)]
    return num_list
def find_sum(num_list:list)-> int:
    """находит сумму элементов на нечетных позициях"""
    sum=0
    print('числа на нечетных позициях -> ',end=' ')
    for i in range(len(num_list)):
        if i%2:
            continue
        else:
            print(num_list[i],end=' ')
            sum+=num_list[i]
    print()
    return sum
def mult_list(list_num:list)->list:
    """находит произведение пар чисел, первое с последним и тд"""
    result=[]
    end_size=len(list_num)-1
    for i in range(len(list_num)):
        if i==end_size:
            result.append(list_num[i])
            break
        elif end_size<i:
            break
        else:
            result.append(list_num[i]*list_num[end_size])
            end_size-=1
    return result
def bin_dig(num):
    
    if num==0:
        return num
    else:
        bin_num.append(num%2)
        bin_dig(num=num//2)
def fibonacci(num:int)->[]:
    """пересчет Фибоначи для отрицательного или положительного чисел"""
    if num>=0:
       num_list = range(num+1)
       a = [0,1]
       for k in num_list[2:]:
           a.append(a[k-1] + a[k-2]) 
       return a[num]
    else:
       num=-(num-1)
       num_list = range(num+1)
       a = [1,0]
       for k in num_list[2:]:
           a.append(a[k-2] - a[k-1]) 
       a.reverse()
    return a[0]
#1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
#стоящих на нечётной позиции.
#Пример:
#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
try:
    num=create_list(int(input('введите размер генерируемого списка ')))
    print(num)
    print(f'сумма чисел на нечетных позициях -> {find_sum(num)}')

#2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16];
#[2, 3, 5, 6] => [12, 15]
    print(f'нахождение произведений пар чисел\n список-> {num}')
    print(f'произведение пар -> {mult_list(num)}')
#3-Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#[1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
#[4.07, 5.1, 8.2444, 6.98] - 0.91 или 91
    float_num=[round(random.uniform(-20,20),3) for i in range(int(input('введите размер списка\
для вещественных чисел -> ')))]
    print(float_num)
    del num
    num=[]
    for i in range(len(float_num)):
        num.append(math.fabs(float_num[i]-int(float_num[i])))
    i_min=num[0]
    i_max=num[0]
    for i in range(len(num)):
        if i_min>num[i]:
            i_min=num[i]
        elif i_max<num[i]:
            i_max=num[i]
    result=round(i_max-i_min,3)
    print(f'максимальное значение дробной части в числе {round(i_max,3)}\n\
минимальное значение дробной части в числе {round(i_min,3)}\n\
разница дробной части = {result}' )
        
#4- Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Подумайте, как это можно решить с помощью рекурсии.
#Пример:
#45 -> 101101
#3 -> 11
#2 -> 10
    bin_num=[]
    print('преобразование из системы с основанием 10, в двоичную сиси.тему')
    n=bin_dig(int(input('введите число ->')))
    bin_num.reverse()
    for i in bin_num:
        print(i,end='')
    print()

#5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Негафибоначчи
#Решение оформлять в виде функций
#По возможности добавляйте docstring
    fib=int(input('введите число для списка Фибоначчи\негаФибоначчи -> '))
    print('последовательность Фибоначчи -> ')
    nfib=fib*(-1)
    if fib<0:
        for i in range(fib,0):
            print(fibonacci(i),end=' ')
        print()
    else:
        for i in range(fib+1):
            print(fibonacci(i),end=' ')
        print()
    for i in range(nfib,fib+1):
        print(fibonacci(i),end=' ')
    print(' ')

except ValueError: 
    print('не верные данные')