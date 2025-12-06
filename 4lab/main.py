'''примем число П за 3,14'''


class Triangle():
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)
        self.x3 = int(x3)
        self.y3 = int(y3)

    def area(self):
        dlina1 = ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5
        dlina2 = ((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2) ** 0.5
        dlina3 = ((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2) ** 0.5
        if dlina1 + dlina3 > dlina2 and dlina1 + dlina2 > dlina3 and dlina3 + dlina2 > dlina1:
            p = (dlina1 + dlina2 + dlina3) / 2
            s = (p * (p - dlina1) * (p - dlina2) * (p - dlina3)) ** 0.5
            return round(s, 2)
        else:
            return 'Такого треугольника не существует'

    def perimeter(self):
        dlina1 = ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5
        dlina2 = ((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2) ** 0.5
        dlina3 = ((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2) ** 0.5
        if dlina1 + dlina3 > dlina2 and dlina1 + dlina2 > dlina3 and dlina3 + dlina2 > dlina1:
            p = dlina1 + dlina2 + dlina3
            return round(p, 2)
        else:
            return 'Такого треугольника не существует'

    def vertices(self):
        return 3


class Rectangle():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)

    def area(self):
        dlina1 = abs(self.x1 - self.x2)
        dlina2 = abs(self.y1 - self.y2)
        s = dlina1 * dlina2
        return round(s, 2)

    def perimeter(self):
        dlina1 = abs(self.x1 - self.x2)
        dlina2 = abs(self.y1 - self.y2)
        p = (dlina1 + dlina2) * 2
        return round(p, 2)

    def vertices(self):
        return 4


class Circle():
    def __init__(self, x1, y1, r):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.r = int(r)

    def area(self):
        s = self.r ** 2 * 3.14
        return round(s, 2)

    def perimeter(self):
        p = 2 * self.r * 3.14
        return round(p, 2)

    def vertices(self):
        return 0


m = int(input('Введите количество фигур '))
mas = []
for i in range(m):
    a = input()
    mas.append(a)
b = input()
if b not in 'area, perimeter, vertices':
    print('Введите area, perimeter или vertices')
sum_area = 0
sum_per = 0
sum_vert = 0
for elem in mas:
    c = (elem + ' ' + b).split()
    if c[0] == 'triangle':
        if len(c) != 8:
            print('Введите верное количество координат')
        else:
            if c[-1] == 'area':
                k = Triangle(c[1], c[2], c[3], c[4], c[5], c[6])
                print('Площадь треугольника:', k.area())
                sum_area += k.area()
            if c[-1] == 'perimeter':
                k = Triangle(c[1], c[2], c[3], c[4], c[5], c[6])
                print('Периметр треугольника:', k.perimeter())
                sum_per += k.perimeter()
            if c[-1] == 'vertices':
                k = Triangle(c[1], c[2], c[3], c[4], c[5], c[6])
                print('Количество углов треугольника:', k.vertices())
                sum_vert += k.vertices()

    if c[0] == 'rectangle':
        if len(c) != 6:
            print('Введите верное количество координат')
        else:
            if c[-1] == 'area':
                k = Rectangle(c[1], c[2], c[3], c[4])
                print('Площадь прямоугольника:', k.area())
                sum_area += k.area()
            if c[-1] == 'perimeter':
                k = Rectangle(c[1], c[2], c[3], c[4])
                print('Периметр прямоугольника:', k.perimeter())
                sum_per += k.perimeter()
            if c[-1] == 'vertices':
                k = Rectangle(c[1], c[2], c[3], c[4])
                print('Количество углов прямоугольника:', k.vertices())
                sum_vert += k.vertices()

    if c[0] == 'circle':
        if len(c) != 5:
            print('Введите верное количество координат')
        else:
            if c[-1] == 'area':
                k = Circle(c[1], c[2], c[3])
                print('Площадь круга:', k.area())
                sum_area += k.area()
            if c[-1] == 'perimeter':
                k = Circle(c[1], c[2], c[3])
                print('Периметр круга:', k.perimeter())
                sum_per += k.perimeter()
            if c[-1] == 'vertices':
                k = Circle(c[1], c[2], c[3])
                print('Количество углов круга:', k.vertices())
                sum_vert += k.vertices()

if b == 'area':
    print('Total area:', sum_area)
if b == 'perimeter':
    print('Total perimeter:', sum_per)
if b == 'vertices':
    print('Total vertices:', sum_vert)
'''
triangle 4 0 0 3 0 0
triangle 0 0 3 0 5 6
rectangle 0 0 3 2
circle 1 1 5
perimeter
'''
