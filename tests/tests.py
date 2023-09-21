import os
import sys
import unittest


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE_DIR_PATH = os.path.join(BASE_DIR, 'code')
sys.path.append(CODE_DIR_PATH)


from FigureArea import figure_area, angle


class TestArea(unittest.TestCase):
    """Класс для тестирования вычислений площади с помощью figure_area"""

    def test_lenght_sides(self):
        call = figure_area(a=4, b=4, c=90)
        result = 'фигура не является треугольником'
        self.assertEqual(
            call, result, 'Функция figure_area должна работать '
                          'с корректными длинами сторон треугольника'
        )

    def test_positive_integers_triangle(self):
        call = figure_area(a=-4, b=-4, c=-2)
        result = 'фигура не является треугольником'
        self.assertEqual(
            call, result, 'Длины сторон должны быть положительными числами'
        )

    def test_quantity_arguments(self):
        call = figure_area(a=4, b=4)
        result = (
            'введены не все аргументы, либо радиус введен '
            'совместно со сторонами треугольника'
        )
        self.assertEqual(
            call, result, 'Функция принимает либо три стороны треугольника, '
                          'либо радиус круга'
        )


class TestAngle(unittest.TestCase):
    """
    Класс для тестирования проверки треугольника на
    прямоугольник с помощью check_angle
    """

    def test_angle(self):
        call = angle(a=1, b=3, c=3)
        result = 'треугольник не является прямоугольным'
        self.assertEqual(
            call, result, 'функция должна определять прямоугольный треугольник'
        )


if __name__ == '__main__':
    unittest.main()
