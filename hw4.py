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
#             N %= 10
#             print(N)
# else:
#     print('Введите верное количество элементов после запятой...')


# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.




# 3. Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

# 4. Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0