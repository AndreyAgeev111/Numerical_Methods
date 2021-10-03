def fancy_print(A, B, selected):
    for row in range(len(B)):
        print("(", end='')
        for col in range(len(A[row])):
            print("\t{1:10.2f}{0}".format(" " if (selected is None
                                                  or selected != (row, col)) else "*", A[row][col]), end='')
        print("\t) * (\tX{0}) = (\t{1:10.2f})".format(row + 1, B[row]))


def swap_rows(A, B, row1, row2):
    A[row1], A[row2] = A[row2], A[row1]
    B[row1], B[row2] = B[row2], B[row1]


def divide_row(A, B, row, divider):
    if divider == 0:
        return 0
    A[row] = [a / divider for a in A[row]]
    B[row] /= divider


def combine_rows(A, B, row, source_row, weight):
    A[row] = [(a + k * weight) for a, k in zip(A[row], A[source_row])]
    B[row] += B[source_row] * weight


def Gauss(A, B, for_r_a, for_r_b):
    column = 0
    flag = 0
    while column < len(B):
        print("Ищем максимальный по модулю элемент в {0}-м столбце:".format(column + 1))
        current_row = None
        for r in range(column, len(A)):
            if current_row is None or abs(A[r][column]) > abs(A[current_row][column]):
                current_row = r
        if current_row is None:
            print("решений нет")
            return None
        fancy_print(A, B, (current_row, column))
        if current_row != column:
            print("Переставляем строку с найденным элементом повыше:")
            swap_rows(A, B, current_row, column)
            fancy_print(A, B, (column, column))
        print("Нормализуем строку с найденным элементом:")
        divide_row(A, B, column, A[column][column])
        fancy_print(A, B, (column, column))
        if divide_row(A, B, column, A[column][column]) == 0:
            print("Получено множество решений")
            flag =+ 1
            break
        print("Обрабатываем нижележащие строки:")
        for r in range(column + 1, len(A)):
            combine_rows(A, B, r, column, -A[r][column])
        fancy_print(A, B, (column, column))
        column += 1
    if flag == 1:
        return 0
    print("Матрица приведена к треугольному виду, считаем решение")
    X = [0 for _ in B]
    for i in range(len(B) - 1, -1, -1):
        X[i] = B[i] - sum(x * a for x, a in zip(X[(i + 1):], A[i][(i + 1):]))
    print("Получили ответ:")
    print("\n".join("X{0} =\t{1:10.2f}".format(i + 1, x) for i, x in
                    enumerate(X)))
    print("Посчитаем общую невязку:")
    r = 0
    coefficients_multiply = 0
    for i in range(len(B)):
        for j in range(len(B)):
            coefficients_multiply += X[j] * for_r_a[i][j]
        r += for_r_b[i] - coefficients_multiply
        coefficients_multiply = 0
    print(r)
    return X


my_a = [
    [1.0, 1.0, 2.0, 3.0],
    [1.0, 2.0, 3.0, -1.0],
    [3.0, -1.0, -1.0, -2.0],
    [2.0, 3.0, -1.0, -1.0]
]

my_b = [
    1.0,
    -4.0,
    -4.0,
    -6.0]


my_a_for_r = [
    [1.0, 1.0, 2.0, 3.0],
    [1.0, 2.0, 3.0, -1.0],
    [3.0, -1.0, -1.0, -2.0],
    [2.0, 3.0, -1.0, -1.0]
]

my_b_for_r = [
    1.0,
    -4.0,
    -4.0,
    -6.0]


def Gauss_method():
    fancy_print(my_a, my_b, None)
    Gauss(my_a, my_b, my_a_for_r, my_b_for_r)
