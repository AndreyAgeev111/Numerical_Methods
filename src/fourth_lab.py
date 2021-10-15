import numpy as np
import matplotlib.pyplot as plt


def function(x):
    return 2 * x ** 2 - x * 3 - 5.7899


def show_fun():
    x = np.linspace(-10, 10, 1000)
    plt.plot(x, function(x))
    plt.xlim([-10, 10])
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(r'$y = x^2 - 3*x - 5.7899$')
    plt.show()


def poly_newton_coefficient(x, y):
    m = len(x)

    x = np.copy(x)
    a = np.copy(y)
    for k in range(1, m):
        a[k:m] = (a[k:m] - a[k - 1]) / (x[k:m] - x[k - 1])

    return a


def Newton_polynomial(x_data, y_data, x):
    a = poly_newton_coefficient(x_data, y_data)
    n = len(x_data) - 1
    p = a[n]

    for k in range(1, n + 1):
        p = a[n - k] + (x - x_data[n - k]) * p

    return p


def show_Newton():
    x = np.linspace(-10, 10, 21)
    x_data = np.linspace(-10, 10, 21)
    y_data = function(x_data)

    print("Таблица значений для изначальной функции:")
    for x_values in x_data:
        print(f'|| x = {x_values} || y = {round(function(x_values), 4)} ||')

    p = Newton_polynomial(x_data, y_data, x)

    print("Таблица значений для полинома Ньютона:")
    for i in range(len(p)):
        print(f'|| x = {x[i]} || y = {round(p[i], 4)} ||')

    plt.scatter(x_data, y_data, color="green", label="Изначальная функция")
    plt.plot(x, p, linestyle="dotted", color="blue", label="Полином Ньютона")
    plt.xlim([-10, 10])
    plt.grid()
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(r'$y = x^2 - 3*x - 5.7899$')
    plt.show()


class SplineTuple:
    def __init__(self, a, b, c, d, x):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.x = x


def build_spline(x, y, n):
    splines = [SplineTuple(0, 0, 0, 0, 0) for _ in range(0, n)]
    for i in range(0, n):
        splines[i].x = x[i]
        splines[i].a = y[i]

    splines[0].c = splines[n - 1].c = 0.0

    alpha = [0.0 for _ in range(0, n - 1)]
    beta = [0.0 for _ in range(0, n - 1)]

    for i in range(1, n - 1):
        hi = x[i] - x[i - 1]
        hi1 = x[i + 1] - x[i]
        A = hi
        C = 2.0 * (hi + hi1)
        B = hi1
        F = 6.0 * ((y[i + 1] - y[i]) / hi1 - (y[i] - y[i - 1]) / hi)
        z = (A * alpha[i - 1] + C)
        alpha[i] = -B / z
        beta[i] = (F - A * beta[i - 1]) / z

    for i in range(n - 2, 0, -1):
        splines[i].c = alpha[i] * splines[i + 1].c + beta[i]

    for i in range(n - 1, 0, -1):
        hi = x[i] - x[i - 1]
        splines[i].d = (splines[i].c - splines[i - 1].c) / hi
        splines[i].b = hi * (2.0 * splines[i].c + splines[i - 1].c) / 6.0 + (y[i] - y[i - 1]) / hi
    return splines


def cubic_interpolate(splines, x):
    if not splines:
        return None

    n = len(splines)

    i = 0
    j = n - 1
    while i + 1 < j:
        k = i + (j - i) // 2
        if x <= splines[k].x:
            j = k
        else:
            i = k
    s = splines[j]

    dx = x - s.x

    return s.a + (s.b + (s.c / 2.0 + s.d * dx / 6.0) * dx) * dx


def cubic_interpolation_show():
    x = np.linspace(-10, 10, 21)
    y = function(x)
    x_new = np.linspace(-10, 10, 201)
    plt.scatter(x, y, color="green", label="Изначальная функция")
    plt.xlim([-10, 10])
    spline = build_spline(x, y, 21)
    y_new = np.empty(len(x_new))
    for i in range(len(x_new)):
        y_new[i] = cubic_interpolate(spline, x_new[i])
    plt.plot(x_new, y_new, linestyle="dotted", color="blue", label="Кубическая интерполяция")
    plt.grid()
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(r'$y = x^2 - 3*x - 5.7899$')
    plt.show()
