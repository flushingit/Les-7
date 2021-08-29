# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: см. в методичке.
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        a = ""
        max_len = 0
        for x in self.matrix:  # Определяем самый длинный элемент для выравнивания столбцов матрицы
            for y in x:
                if len(str(y)) > len(str(max_len)):
                    max_len = y

        for x in self.matrix:
            for y in x:
                # Склеиваем строку из элемента матрицы с добавлением пробелов соответственно длинне элемента
                a = a + str(y) + " " * (int((len(str(max_len)) - len(str(y))) + 1))

            a = a + '\n'  # Разбиваем строку
        return a

    def __add__(self, other):

        def get_val(name, x, y):
            """Получаем значение в координатах матрицы, если значение за пределами матрицы возвращаем 0"""
            try:
                a = name[x][y]
                return a
            except IndexError:
                return 0

        m3 = []
        for x in range(max(len(self.matrix), len(other.matrix))):  # Создаём в матрице максмальную длинну столбцов
            n = []
            for y in range(
                    max(len(self.matrix[0]), len(other.matrix[0]))):  # Создаём в матрице максмальную длинну строк
                n.append(get_val(self.matrix, x, y) + get_val(other.matrix, x, y))  # Складываем элементы в строке
            m3.append(n)  # Добавляем строку в матрицу
        return m3


def matrix_construct():
    """Формируем список для передачи в класс"""
    matrix = []
    a = input("Введите строку матрицы через пробел ")
    check = len([x for x in a.split()])
    matrix.append([float(x) for x in a.split()])
    while True:
        a = input("Введите строку матрицы через пробел , выход - пустая строка ")
        if a == "":
            break
        elif len([x for x in a.split()]) != check:
            print(len([x for x in a.split()]))
            print(f"Количество переменных должно быть {check}")

        else:
            x_str = [float(x) for x in a.split()]

            matrix.append(x_str)

    return matrix


print("Введите первую матрицу")
m1 = Matrix(matrix_construct())
print("Введите вторую матрицу")
m2 = Matrix(matrix_construct())
m3 = Matrix(m1 + m2)
print("Первая матрица")
print(m1)
print("Вторая матрица")
print(m2)
print("Результат сложения матриц")
print(m3)
