import math


class Figure:
    sides_count = 0  # Атрибут класса, количество сторон

    def __init__(self, sides, color, filled=False):
        if len(sides) != self.sides_count:
            sides = [1] * self.sides_count  # Создаем массив с единичными сторонами
        self.__sides = sides  # Инкапсуляция списка сторон
        self.__color = color  # Инкапсуляция цвета в формате RGB
        self.filled = filled  # Публичный атрибут, закрашенный или нет

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return isinstance(r, int) and isinstance(g, int) and isinstance(b, int) and \
            0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, color):
        if isinstance(color, tuple) and len(color) == 3 and all(0 <= c <= 255 for c in color):
            self.__color = color
        else:
            self.__color = self.__color

    def __is_valid_sides(self, *sides):
        if all(isinstance(side, (int, float)) and side > 0 for side in sides):
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, new_sides):
        self.__sides = new_sides

    def info(self):
        return {"sides": self.__sides, "color": self.__color, "filled": self.filled}


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference, filled=False):
        if circumference <= 0:
            print("Значение должно быть положительным")
        radius = self.calculate_radius(circumference)
        super().__init__([circumference], color, filled)
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    @staticmethod
    def calculate_radius(circumference):
        if circumference <= 0:
            print("Значение должно быть положительным")
        return circumference / (2 * math.pi)

    def set_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            raise ValueError(f"Must provide exactly {self.sides_count} positive side.")
        super().set_sides(*new_sides)
        self.__radius = self.calculate_radius(new_sides[0])  #

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def info(self):
        return {"type": "Circle", "circumference": self.get_sides(), "radius": self.get_radius(),
                "square": self.get_square(), "filled": self.filled, "color": self.get_color()}

    def __len__(self):
        return int(2 * math.pi * self.__radius)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, a, b, c, color, filled=False):
        sides = [a, b, c]
        if len(sides) != self.sides_count:
            sides = [1] * self.sides_count

        if not all(side > 0 for side in sides) or not self.is_valid_triangle(*sides):
            print("Недопустимые стороны треугольника")

        super().__init__(sides, color, filled)
        self.__sides = sides

    def is_valid_triangle(self, a, b, c):
        return a + b > c and a + c > b and b + c > a

    def get_sides(self):
        return self.__sides

    def set_sides(self, sides):
        if len(sides) != 3 or not all(isinstance(side, (int, float)) and side > 0 for side in sides):
            print("Значения должны быть положительными")

        if not self.is_valid_triangle(*sides):
            print("Недопустимые стороны треугольника")

        super().set_sides(sides)
        self.__sides = sides

    def get_square(self):
        s = sum(self.__sides) / 2  # Полупериметр
        area = math.sqrt(s * (s - self.__sides[0]) * (s - self.__sides[1]) * (s - self.__sides[2]))
        return area

    def info(self):
        return {"type": "Triangle", "sides": self.get_sides(), "area": self.get_square(),
                "filled": self.filled, "color": self.get_color()}


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length, filled=False):
        sides = [side_length] * Cube.sides_count  # Список из 12 одинаковых сторон
        super().__init__(sides, color, filled)

    def set_sides(self, *new_side_lengths):
        if len(new_side_lengths) == 1:
            new_side_length = new_side_lengths[0]
            if new_side_length <= 0:
                print("Длина стороны должна быть положительной.")
            super().set_sides([new_side_length] * Cube.sides_count)
            return f"Sides updated to {new_side_length}."
        else:
            pass

    def get_volume(self):
        return self.get_sides()[0] ** 3

    def info(self):
        return {"type": "Cube", "volume": self.get_volume(), "sides": self.get_sides(), "filled": self.filled,
                "color": self.get_color()}


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
# Проверка на изменение цветов:
circle1.set_color((55, 66, 77))  # Изменится
print(circle1.get_color())
cube1.set_color((300, 70, 15))  # Не изменится
print(cube1.get_color())
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
# Проверка периметра (круга), это и есть длина:
print(len(circle1))
# Проверка объёма (куба):
print(cube1.get_volume())
print(' ')
print('__Свои проверки__')
print(' ')
print('Описание: ', circle1.info())
print('Радиус: ', circle1.get_radius())
print('Площадь: ', circle1.get_square())
print('Периметр: ', len(circle1))
circle1.set_sides(55)
print('Новая сторона : ', circle1.get_sides())
print('Радиус: ', circle1.get_radius())
print('Площадь: ', circle1.get_square())
print('Описание: ', circle1.info())
print('Периметр: ', len(circle1))
triangle1 = Triangle(5, 6, 9, (200, 200, 100))
print('Описание: ', triangle1.info())
print('Площадь: ', triangle1.get_square())
print('Периметр: ', len(triangle1))
triangle1.set_color((55, 66, 77))
triangle1.set_sides((41, 55, 67))
print('Описание: ', triangle1.info())
print('Площадь: ', triangle1.get_square())
print('Периметр: ', len(triangle1))
print(cube1.get_sides())
print('Цвет: ', cube1.get_color())
print('Описание: ', cube1.info())
print('Цвет: ', cube1.get_color())
cube1.set_color((200, 70, 15))
print('Цвет: ', cube1.get_color())
print('Объем: ', cube1.get_volume())
cube1.set_sides(75)
print(cube1.get_sides())
print('Объем: ', cube1.get_volume())
print('Описание: ', cube1.info())
