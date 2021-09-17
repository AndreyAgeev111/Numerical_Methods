import math
import numpy as np
import matplotlib.pyplot as plt

ROOT = 1
ACCURACY = 0.001


def func(x):
    return 1 / x - x ** 2


# Производная функции


def func_derivative(x):
    return - (1 / (x ** 2)) - 2 * x


def show_func():
    x = np.linspace(0.01, 5, 1000)
    plt.plot(x, func(x))
    plt.xlim([0, 5])
    plt.ylim([-1, 5])
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('$y = 1 / x - x^2$')
    plt.show()


def tangent_method():
    # точка, являющаяся границей выбранного нами участка, лежит ближе всего к корню
    b = 0.2
    # Вписать любое значение большее b, чтобы первое условие цикло верно выполнилось
    iter = 1

    while True:
        root = b
        b = b - func(b) / func_derivative(b)
        if b - root < ACCURACY:
            break
        print(f'{iter} итерация, корень = {b}')
        iter += 1
    print(f'Корень = {root}, корень вычисленный аналитически = {ROOT}')


def chord_method():
    # участок, где лежит корень
    a = 0.1
    b = 3
    calc_a = (b * func(a) - a * func(b)) / (func(a) - func(b))
    # для выполнения первого условия цикла, боже спаси do-while в питоне((
    iter = 1

    while True:
        root = calc_a
        calc_a = (b * func(calc_a) - calc_a * func(b)) / (func(calc_a) - func(b))
        if root - calc_a <= ACCURACY:
            break
        print(f'{iter} итерация, корень = {calc_a}')
        iter += 1
    print(f'Корень = {root}, корень вычисленный аналитически = {ROOT}')


# Метод простых итераций, обозначим функцию через 2 составляющие функции


def first_func(x):
    return 1 / x


def second_func(x):
    return x ** 2


# Производные функций


def first_func_derivative(x):
    return - 1 / (x ** 2)


def second_func_derivative(x):
    return 2 * x


def simple_iterations_method():
    a = 0.5
    # выясняем,чья производная функции в точке будет меньше, чтобы выбрать ее первой для метода
    if first_func_derivative(a) > second_func_derivative(a):
        calc_a = a
        func_a = second_func(calc_a)
        iter = 1
        x_coord = [calc_a]
        y_coord = [func_a]

        while True:
            root = calc_a
            calc_a = 1 / func_a
            func_a = second_func(calc_a)
            print(f'{iter} итерация, корень = {calc_a}')
            if abs(abs(root) - abs(calc_a)) <= ACCURACY:
                break
            iter += 1
            x_coord.append(calc_a)
            y_coord.append(func_a)
        print(f'Корень = {root}, корень вычисленный аналитически = {ROOT}')
    else:
        calc_a = a
        func_a = first_func(calc_a)
        iter = 1
        x_coord = [calc_a]
        y_coord = [func_a]

        while True:
            root = calc_a
            calc_a = math.sqrt(func_a)
            func_a = first_func(calc_a)
            print(f'{iter} итерация, корень = {calc_a}')
            if abs(abs(root) - abs(calc_a)) <= ACCURACY:
                break
            iter += 1
            x_coord.append(calc_a)
            y_coord.append(func_a)
        print(f'Корень = {root}, корень вычисленный аналитически = {ROOT}')

        x = np.linspace(0.01, 5, 1000)
        plt.plot(x, first_func(x), label="$1 / x$")
        plt.plot(x, second_func(x), label="$x^2$")
        plt.plot(x_coord, y_coord, label="$решение$")
        plt.xlim([0.5, 1.5])
        plt.ylim([0.6, 2])
        plt.grid()
        plt.legend()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('$1 / x = x^2$')
        plt.show()
