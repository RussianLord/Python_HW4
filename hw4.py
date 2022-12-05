# 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# ПЕРВЫЙ ВАРИАНТ:
# N = float(input('Введите число с значениями после запятой... '))
# S = int(input('Введите количество знаков после запятой... '))

# if 0 < S < 11:
#     print(round(N, S))
# else:
#     print('Введите верное количество элементов после запятой...')

# ВТОРОЙ ВАРИАНТ:
# N = float(input('Введите число с значениями после запятой... '))
# S = input('Введите число с значениями после запятой для обрезки оригинала... ').split('.')
# if 0 < len(S[1]) < 11:
#     print(round(N, len(S[1])))
# else:
#     print('Введите верное количество элементов после запятой...')

# ТРЕТИЙ ВАРИАНТ: НЕ ОСИЛИЛ
# N = float(input('Введите число с значениями после запятой... '))
# S = input('Введите число с значениями после запятой для обрезки оригинала... ').split('.')
# idx = 0
# X = len(str(N).split('.')[0])
# if 0 < len(S[1]) < 11:
#     while len(S[1]) != len(str(N).split('.')[1]):
#         N *= 10
#         idx += 1
#     else:
#         while X != len(str(N).split('.')[0]):
#             float(N)
#             N //= 10
#             print(N)
# else:
#     print('Введите верное количество элементов после запятой...')


# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# N = int(input())

# for i in range(1, N):
#     if N % i == 0:
#         print(i)
#     else:
#         i += 1

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

# listN = list(input('Введите числа для списка....').split())
# listNew = []
# for i in listN: 
#     if i not in listNew:
#         listNew.append(i)
# print(listNew)

# number_set = set()
# out_list = []
# some_list = list(map(int, input().split()))
# for ind in range(0, len(some_list)):
#     if some_list[ind] not in number_set:
#         number_set.add(some_list[ind])
#         for ind1 in range(ind + 1, len(some_list)):
#             if some_list[ind] == some_list[ind1]:
#                 break
#         else:
#             out_list.append(some_list[ind])
# print(out_list)

# some_list = list(map(int, input().split()))
# for i in some_list:
#     if some_list.count(i) == 1:
#         print(i, end=' ')


# 4. Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
K = int(input('Введите степень... '))
diff = 0
for i in range(K):
    S = int(random.randint(0, 10))
    if S != 0:
        diff = diff + S**K
        print(f'{S}^{K}({S**K}) + ', end='')
        K = K - 1
        
        
S = int(random.randint(0, 10))
if S != 0:    
    print(S, end=' = ')
    print(diff + S)
else:
    print(end=' = ')
    print(diff)
