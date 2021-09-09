import math
import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return x * np.log(x) - x / 2


def func_backward(x):
    return 0.5 + np.log(x)


def show_func():
    x = np.linspace(0.01, 5, 1000)
    plt.plot(x, func(x))
    plt.xlim([0, 5])
    plt.ylim([-1, 5])
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('$y = x * ln(x) - x / 2$')
    plt.show()


def tangent_method():
    # точка, являющаяся границей выбранного нами участка, лежит ближе всего к корню
    b = 2
    # Вписать любое значение большее b, чтобы первое условие цикло верно выполнилось
    root = 3
    iter = 1

    while root - b >= 0.001:
        root = b
        b = b - func(b) / func_backward(b)
        print(str(iter) + " итерация, корень = " + str(b))
        iter += 1
    root = b
    print("Корень = " + str(root) + ", корень вычисленный аналитически = " + str(math.sqrt(np.e)))


def chord_method():
    # участок, где лежит корень
    a = 1
    b = 2
    calc_a = (b * func(a) - a * func(b)) / (func(a) - func(b))
    # для выполнения первого условия цикла, боже спаси do-while в питоне((
    root = a
    iter = 1

    while calc_a - root >= 0.001:
        root = calc_a
        calc_a = (b * func(calc_a) - calc_a * func(b)) / (func(calc_a) - func(b))
        print(str(iter) + " итерация, корень = " + str(calc_a))
        iter += 1
    root = calc_a
    print("Корень = " + str(root) + ", корень вычисленный аналитически = " + str(math.sqrt(np.e)))


def simple_iterations_method():
    return 0
