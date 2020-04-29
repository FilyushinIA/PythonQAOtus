import math


class Figure(object):

    def __init__(self, name):
        self.name = name
        self._area = 0
        self._angles = 0
        self._perimeter = 0

    @property
    def area(self):
        return self._area

    @property
    def angles(self):
        return self._angles

    @property
    def perimeter(self):
        return self._perimeter

    def add_square(self, figure):
        if isinstance(figure, Figure):
            return self._area + figure._area
        else:
            return'Передан неправильный класс'


class Rectangle(Figure):

    def __init__(self, width, height):
        super().__init__('Прямоугольник')
        self.width = width
        self.height = height
        self._area = width * height
        self._angles = 4
        self._perimeter = 2 * (width + height)


class Square(Rectangle):

    def __init__(self, width):
        super().__init__(width, width)
        self.name = 'Квадрат'


class Triangle(Figure):

    def __init__(self, *args):
        super().__init__('Треугольник')
        assert len(args) == 3, "Необходимы длин трёх сторон"
        s1, s2, s3 = [x for x in args]
        self._angles = 3
        self._perimeter = p = sum(args)
        self._area = math.sqrt(p * (p - s1) * (p - s2) * (p - s3))


class Circle(Figure):

    def __init__(self, radius):
        super().__init__('Круг')
        self._angles = 0
        self._perimeter = p = 2 * math.pi * radius
        self._area = math.pi * radius * radius
