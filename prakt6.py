#задание 1
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print("matrix:")
# for row in matrix:
#   print(row)

# print("нечётные числа matrix")
# odd_numbers = []
# for row in matrix:
#  for num in row:
#      if num % 2 != 0:
#       odd_numbers.append(num)

# print(num, end=" ")

# print("кол-во чётных:", sum(1 for row in matrix for num in row if num % 2 == 0))
#задание 2
# matrix_1 = [[2, 4, 3, 6], [5, 7, 1, 5]]
# matrix_2 = [[2, 9, 0, 2], [3, 4, 7, 6]]

# answer_matrix = [[0 for _ in range(len(matrix_1[0]))] for _ in range(len(matrix_1))]

# for i in range(len(matrix_1)):
#      for j in range(len(matrix_1[0])):
#          answer_matrix[i][j] = matrix_1[i][j] * matrix_2[i][j]

# print(answer_matrix)
# #вывод сумм
# for i in range(len(answer_matrix)):
#  row_sum = sum(answer_matrix[i])
#  print(f"{answer_matrix[i]} сумма строки: {row_sum}")
#задание 3
# fruits = [['Banana', 'apple'], ['apricot', 'Avocado'], ['lime', 'lemon'], ['Mango', 'grapes']]

# print("Элементы с заглавной буквы:")
# for row in fruits:
#      for fruit in row:
#          if fruit[0].isupper():
#              print(fruit)
#задание 4
# fruits = ['apple', 'banana', 'cherry']
# for index, fruit in enumerate(fruits):
#     print(f"Индекс: {index}, Фрукт: {fruit}")
#Задание 5
# rows = int(input("Введите количество строк: "))
# cols = int(input("Введите количество столбцов: "))
# matrix = []
# for i in range(rows):
#     row = []
#     for j in range(cols):
#         value = int(input(f"Введите значение элемента [{i}][{j}]: "))
#         row.append(value)
#     matrix.append(row)

# # Вывод матрицы
# print("Ваш двумерный массив:")
# for row in matrix:
#     print(row)