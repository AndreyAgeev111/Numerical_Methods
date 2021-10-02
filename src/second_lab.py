import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

A, B = 1, 3
N = 10000
SUM = 5.72291136766
H = (B - A) / N
X = np.linspace(A, B, N)


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
    sum = 0
    for i in range(N - 1):
        sum += func((X[i] + X[i + 1]) / 2) * H

    print(f'Значение интеграла = {sum}, вычисленное с помощью специализированного ПО = {SUM}')


def trapezoid_method():
    sum = 0
    for i in range(N - 1):
        sum += ((func(X[i]) + func(X[i + 1])) / 2) * H

    print(f'Значение интеграла = {sum}, вычисленное с помощью специализированного ПО = {SUM}')


def simpson_method():
    sum = 0
    for i in range(1, N):
        sum += (func(X[i - 1]) + 4 * func((X[i - 1] + X[i]) / 2) + func(X[i])) / 6 * H

    print(f'Значение интеграла = {sum}, вычисленное с помощью специализированного ПО = {SUM}')