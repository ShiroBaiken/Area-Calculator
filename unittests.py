import unittest
from figures import Figure, Circle, Triangle
from figure_fabriq import FigureFactory


class TestCircle(unittest.TestCase):

    def test_zero(self):
        circle = Circle(0)
        self.assertEqual(circle.area(), 0)


class TestTriangle(unittest.TestCase):

    def test_valid_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.sides, [3, 4, 5])
        self.assertTrue(triangle._is_valid_triangle())

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)  # Sum of two sides is not greater than the third side

    def test_right_angled_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.check_90degree())
        self.assertEqual(triangle.area(), 6)

    def test_non_right_angled_triangle_area(self):
        triangle = Triangle(5, 12, 14)
        self.assertFalse(triangle.check_90degree())
        self.assertEqual(triangle.area(), 29.230762904857617)

    def test_square_root_calculation(self):
        triangle = Triangle(8, 15, 17)
        self.assertEqual(triangle.area(), 60)


class TestFactory(unittest.TestCase):

    def test_area(self):
        figures = [Circle, Triangle]
        names = ['circle', 'triangle']
        factory = FigureFactory(figures, names)
        self.assertEqual(factory.calculate_area('triangle', 3, 4, 5), 6)
        self.assertEqual(factory.calculate_area('circle', 2), 12.566370614359172)

    def test_case_ignore(self):
        figures = [Circle, Triangle]
        names = ['circle', 'Triangle']
        factory = FigureFactory(figures, names)
        self.assertEqual(factory.calculate_area('tRiAnGle', 3, 4, 5), 6)

    def test_wrong_name(self):
        figures = [Circle, Triangle]
        names = ['circle', 'triangle']
        factory = FigureFactory(figures, names)
        self.assertRaises(KeyError, factory.chose_factory, 'tr', 3, 5, 6)

    def fest_missing_name(self):
        figures = [Circle, Triangle]
        names = ['circle']
        self.assertRaises(Exception, FigureFactory.__init__, figures, names)

    def test_missing_class(self):
        figures = [Triangle]
        names = ['circle', 'triangle']
        self.assertRaises(Exception, FigureFactory.__init__, figures, names)

    def test_new_class(self):
        class Square(Figure):
            def __init__(self, side):
                self.side = side

            def area(self) -> int | float:
                return self.side ** 2

        figures = [Circle, Triangle, Square]
        names = ['circle', 'triangle', 'square']
        factory = FigureFactory(figures, names)
        self.assertEqual(factory.calculate_area('square', 2), 4)


if __name__ == '__main__':
    unittest.main()
