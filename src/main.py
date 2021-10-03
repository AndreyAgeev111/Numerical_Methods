from src.first_lab import *
from src.second_lab import *
from src.third_lab_Newton import *


def first_lab():
    show_func()
    tangent_method()
    chord_method()
    simple_iterations_method()


def second_lab():
    show_function()
    square_method()
    trapezoid_method()
    simpson_method()


def third_lab():
    Newton_method()
    Gauss_method()


if __name__ == '__main__':
    # Первая лабораторная
    first_lab()
    # Вторая лабораторная
    second_lab()
    # Третья лабораторная
    third_lab()
