import numpy as np
import matplotlib.pyplot as plt
from fourth_lab import poly_newton_coefficient


def function(x):
    return 2 * x ** 2 - x * 3 - 5.7899


def show_fun():
    x = np.linspace(-10, 10, 1000)
    plt.plot(x, function(x))
    plt.xlim([-10, 10])
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(r'$y = 2 * x^2 - 3*x - 5.7899$')
    plt.show()


def calculated_derivative(number):
    h = 1
    derivative = np.empty(111)
    for i in range(111):
        derivative[i] = (- function(number + 2 * h) + 4 * function(number + h) - 3 * function(number)) / h / 2
        h -= 0.009
    return derivative


def classic_derivative(x):
    return 4 * x - 3


def Newton_derivative(number):
    h = 1
    a = np.empty(111)
    for i in range(111):
        x = [number, number + h]
        y = [function(x[0]), function(x[1])]
        a[i] = poly_newton_coefficient(x, y)[1]
        h -= 0.009
    return a


def get_accuracy(x, y):
    return np.abs(x - y)


def show_result():
    show_fun()
    calculated = calculated_derivative(10)[110]
    true = classic_derivative(10)
    newton = Newton_derivative(10)[110]
    print(f'Значение производной в точке x = 10 в виде приближенного численного дифференцирования: '
          f'{calculated}')
    print(f'Значение производной в точке x = 10: {true}')
    print(f'Значение производной в точке x = 10 в виде приближенного численного дифференцирования полиномом Ньютона: '
          f'{newton}')
    print('-----------------------------------------------------------------------------------------------------------')
    print(f'Разность между истинным значением производной и вычисленной с помощью приближенного метода: '
          f'{get_accuracy(true, calculated)}')
    print(f'Разность между истинным значением производной и вычисленной с помощью полинома Ньютона: '
          f'{get_accuracy(true, newton)}')
    show_accuracy_plots(10)


def show_accuracy_plots(number):
    x = np.linspace(0.001, 1, 111)
    plt.plot(x, calculated_derivative(number))
    plt.plot(x, Newton_derivative(number))
    plt.xlim([0, 1])
    plt.grid()
    plt.xlabel('h')
    plt.ylabel('Значение производной')
    plt.title('Сходимость по h значений производной')
    plt.show()

