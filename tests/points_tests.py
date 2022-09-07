import unittest

from emma.points import *


class PointCreationTests(unittest.TestCase):
    def test_correct_creation(self):
        p = Point(x = 1, y = 2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)

    def test_axes_name_validation(self):
        with self.assertRaises(ValueError, msg='Given invalid axis name should raise ValueError.'):
            Point(**{' ': 23})
        with self.assertRaises(ValueError, msg='Trying to name axis as with a reserved name should result in ValueError raise.'):
            Point(dimensions = 4)

    def test_axes_values_validation(self):
        with self.assertRaises(ValueError, msg='Given invalid axis value should raise ValueError.'):
            Point(x = 'x')


class PointTests(unittest.TestCase):
    def setUp(self) -> None:
        self.point = Point(x = 1, y = 2)
        return super().setUp()

    def test_axes_reassignment(self):
        self.point.x = 3
        self.assertEqual(self.point.x, 3)

    def test_reserved_attributes_access(self):
        self.assertEqual(self.point.dimensions, 2)
        self.assertEqual(self.point.axes, {'x', 'y'})

    def test_reserved_attributes_assignment(self):
        with self.assertRaises(AttributeError, msg='When trying to assign to reserved attributes should raise AttributeError.'):
            self.point.dimensions = 3
        with self.assertRaises(AttributeError, msg='When trying to assign to reserved attributes should raise AttributeError.'):
            self.point.axes = {'x', 'y', 'z'}