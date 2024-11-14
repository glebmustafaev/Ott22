class Figure:
    sides_count = 0
    __sides = []
    __color = []
    filled = False

    def __init__(self, rgb, *side):
        self.color = list(rgb)
        self.side = side[0]
        self.filled = True

    def get_color(self):
        self.__color = self.color
        self.filled = True
        return self.__color

    def __is_valid_color(self):
        for i in self.__color:
            if i in range(0, 225):
                return True
            else:
                return False

    def set_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        self.__color = [self.r, self.g, self.b]

    def __is_valid_sides(self):
        for j in self.__sides:
            if j > 0 and len(self.__sides) == self.sides_count:
                return True
            else:
                return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *sides):
        if self.__is_valid_sides(sides):
            self.__sides = sides


class Circle(Figure):
    sides_count = 1
    __radius = None

    def get_square(self):
        return (self.__radius ** 2) * 3.14


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        return (self.side ** 2) * (3 ** 0.5) / 4


class Cube(Figure):
    sides_count = 12

    def list_side(self):
        list_side = []
        for x in range(self.sides_count):
            list_side.append(self.side)
        self.__sides = list_side
        return self.__sides

    def get_volume(self):
        return self.side ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
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
