import math


class Triangle:

    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c

    def check_angle(self):
        sides = [self.a, self.b, self.c]
        hypotenuse = sides.index(max(sides))
        square_hyp = sides.pop(hypotenuse) ** 2
        if sum([i ** 2 for i in sides]) == square_hyp:
            return 'треугольник является прямоугольным'
        else:
            return 'треугольник не является прямоугольным'

    def area(self):
        sides = [self.a, self.b, self.c]
        max_side_value = max(sides)
        del sides[sides.index(max(sides))]
        if (sides[0] + sides[1]) > max_side_value:
            x = (self.a + self.b + self.c) / 2
            return math.sqrt(x * (x - self.a) * (x - self.b) * (x - self.c))
        return 'фигура не является треугольником'


class Circle:

    def __init__(self, r: int) -> None:
        self.r = r

    def area(self):
        return self.r ** 2 * math.pi


def figure_area(a=None, b=None, c=None, r=None):
    """Функция для вычисления площади фигур"""
    if r and not (a and b and c):
        return Circle(r).area()

    elif (a and b and c) and not r:
        return Triangle(a, b, c).area()

    return ('введены не все аргументы, либо радиус введен '
            'совместно со сторонами треугольника')


def angle(a, b, c):
    """Функция проверяет является ли треугольник прямоугольным"""
    return Triangle(a, b, c).check_angle()
