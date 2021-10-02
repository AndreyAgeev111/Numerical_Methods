import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

A, B = 1, 3
N = 10000
SUM = 5.72291136766


def func(x):
    return x ** 2 - x * np.log(x)


def show_func():
    x = np.linspace(0.01, 5)
    fig, ax = plt.subplots()
    ax.plot(x, func(x))
    ax.set_xlim([0, 5])
    ax.set_ylim([0, 7])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('$y = x^2 - x * ln(x)$')

    ix = np.linspace(A, B)
    iy = func(ix)
    verticals = [(A, 0), *zip(ix, iy), (B, 0)]
    poly = Polygon(verticals, facecolor='0.9', edgecolor='0.5')
    ax.add_patch(poly)

    ax.text(0.5 * (A + B), 0.8, r"$\int_a^b f(x)\mathrm{d}x$",
            horizontalalignment='center', fontsize=15)

    plt.show()


def square_method():
    # На сколько кусочков разобьем интервал
    h = (B - A) / N
    x = np.linspace(A, B, N)
    sum = 0
    for i in range(N - 1):
        sum += func((x[i] + x[i + 1]) / 2) * h

    print(f'Значение интеграла = {sum}, вычисленное с помощью специализированного ПО = {SUM}')


def trapezoid_method():
    h = (B - A) / N
    x = np.linspace(A, B, N)
    sum = 0
    for i in range(N - 1):
        sum += ((func(x[i]) + func(x[i + 1])) / 2) * h

    print(f'Значение интеграла = {sum}, вычисленное с помощью специализированного ПО = {SUM}')


def simpson_method():
    h = (B - A) / N
    x = np.linspace(A, B, N)
    sum = 0
    for i in range(1, N):
        sum += (func(x[i - 1]) + 4 * func((x[i - 1] + x[i]) / 2) + func(x[i])) / 6 * h

    print(f'Значение интеграла = {sum}, вычисленное с помощью специализированного ПО = {SUM}')