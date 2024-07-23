import math
from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def area(self) -> int | float:
        pass


class Circle(Figure):

    def __init__(self, rad: int):
        self.rad = rad

    def area(self) -> float:
        """Returns circle area"""
        return math.pi * (self.rad ** 2)


class Triangle(Figure):

    def __init__(self, side1: int, side2: int, side3: int):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

        if not self._is_valid_triangle():
            raise ValueError("Invalid triangle: sum of two sides must be greater than the third side")

    def _is_valid_triangle(self) -> bool:
        """Checks if the triangle is valid (sum of two sides > third side for all combinations)."""
        valid = []
        for i in range(3):
            valid.append(self.sides[i] < sum(self.sides[i+1:] + self.sides[:i]))
        return all(valid)
    @property
    def sides(self) -> list:
        return sorted((self.side1, self.side2, self.side3), reverse=True)

    def check_90degree(self) -> bool:
        if self.sides[0] ** 2 == sum([x ** 2 for x in self.sides[1::]]):
            return True
        else:
            return False

    def area(self) -> int | float:
        """ Adjusts area calculation formula if triangle have 90 degree"""
        if self.check_90degree():
            return (self.sides[1] * self.sides[2]) // 2
        else:
            p = sum(self.sides) / 2
            return math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))



