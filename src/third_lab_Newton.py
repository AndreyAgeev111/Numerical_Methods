import numpy as np
from third_lab_Gauss import *
ACCURACY = 0.001


def first_func(x, y):
    return np.sin(x + 1) - y - 1.2


def second_func(x, y):
    return 2 * x + np.cos(y) - 2


def derivative_first_func_x(x):
    return np.cos(x + 1)


def derivative_first_func_y():
    return -1


def derivative_second_func_x():
    return 2


def derivative_second_func_y(y):
    return - np.sin(y)


def Newton_method():
    x = 0.6
    y = -0.3
    while True:
        root_x = x
        root_y = y
        A = [[derivative_first_func_x(x), derivative_first_func_y()],
                [derivative_second_func_x(), derivative_second_func_y(y)]]
        B = [-first_func(x, y), -second_func(x, y)]
        A_copy = A.copy()
        B_copy = B.copy()
        fancy_print(A, B, None)
        answer = Gauss(A, B, A_copy, B_copy)
        x += answer[0]
        y += answer[1]
        if abs(root_x - x) <= ACCURACY and abs(root_y - y) <= ACCURACY:
            break
    print(f'Корни системы уравнений: x = {x}, y = {y}')
