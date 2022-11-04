from math import sqrt


class Square:

    def __init__(self, edge_length):
        self._side = edge_length
        self._perimeter = 4 * self._side
        self._area = self._side ** 2
        self._diagonal = self._side * sqrt(2)

    def get_side(self):
        return self._side

    def get_perimeter(self):
        return self._perimeter

    def get_area(self):
        return self._area

    def get_diagonal(self):
        return self._diagonal

    @property
    def side(self):
        return self.get_side()

    @property
    def perimeter(self):
        return self.get_perimeter()

    @property
    def area(self):
        return self.get_area()

    @property
    def diagonal(self):
        return self.get_diagonal()

    @side.setter
    def side(self, new_side):
        self._side = new_side
        self._perimeter = 4 * self._side
        self._area = self._side ** 2
        self._diagonal = self._side * sqrt(2)

    @perimeter.setter
    def perimeter(self, new_perimeter):
        self._perimeter = new_perimeter
        self._side = new_perimeter / 4
        self._area = self._side ** 2
        self._diagonal = self._side * sqrt(2)

    @area.setter
    def area(self, new_area):
        self._area = new_area
        self._side = self._area ** 0.5
        self._perimeter = 4 * self._side
        self._diagonal = self._side * sqrt(2)

    @diagonal.setter
    def diagonal(self, new_diagonal):
        self._diagonal = new_diagonal
        self._side = self.diagonal / sqrt(2)
        self._perimeter = 4 * self._side
        self._area = self._side ** 2


square = Square(11)

print(square.get_side())  # 11
print(square.side)        # 11
print(square.perimeter)   # 44

square.perimeter = 48

print(square.get_side())  # 12
print(square.side)        # 12
print(square.perimeter)   # 48
