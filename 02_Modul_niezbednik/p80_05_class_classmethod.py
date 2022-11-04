# @staticmethod - Metody statyczne  - dekorator pozwala wywołać metodę bez instancji, nie przekazuje żadnej wartości
# w pierwszym argumencie - ani self ani cls, możemy ją stosować w innych metodach poprzez
# np. self._chceck_card_number lub cls._check_card_number (dla @classmethod)
# Można się do niej dostać z zewnątrz


from math import pi, sqrt


class Circle:
    def __init__(self, r):
        self.r = r  # in metres

    @classmethod
    def from_area(cls, area):
        radius = sqrt(area / pi)
        return Circle(radius)

    @classmethod #wersja odporna na dziedziczenie (dobra praktyka), odnosi się do klasy cls a nie do konkternej klasy
    def from_diameter(cls, d):
        return cls(d / 2)

    def area(self):
        return pi * self.r ** 2

six = Circle.from_diameter(6)
