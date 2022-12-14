import unittest

from emma.core.points import *


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

    def test_copy_creation(self):
        p1 = Point(x = 1)
        p2 = Point(p1)
        p2.x = 4
        self.assertNotEqual(p1.x, p2.x, msg='Copy creation should create an independent copy.')

    def test_creation_with_overwrite(self):
        p1 = Point(x = 1, y = 1)
        p2 = Point(p1, y = 2)
        self.assertEqual(p1.y, 1)
        self.assertEqual(p2.y, 2)


class PointAttributesAccessTests(unittest.TestCase):
    def setUp(self):
        self.point = Point(x = 1, y = 2)
        return super().setUp()

    def test_axis_reassignment(self):
        self.point.x = 3
        self.assertEqual(self.point.x, 3)

    def test_reserved_attributes_access(self):
        self.assertEqual(self.point.dimensions, 2)
        self.assertEqual(self.point.axes, ('x', 'y'))

    def test_reserved_attributes_assignment(self):
        with self.assertRaises(AttributeError, msg='When trying to assign to reserved attributes should raise AttributeError.'):
            self.point.dimensions = 3
        with self.assertRaises(AttributeError, msg='When trying to assign to reserved attributes should raise AttributeError.'):
            self.point.axes = ('x', 'y', 'z')


class PointAbsoluteValueTests(unittest.TestCase):
    def runTest(self):
        p = Point(x = 3, y = 4)
        self.assertEqual(abs(p), 5)


class PointEqualityTests(unittest.TestCase):
    def setUp(self):
        self.point = Point(y = 1, o = 2, x = 3)

    def test_with_copy(self):
        c = Point(self.point)
        self.assertEqual(self.point, c)

    def test_with_empty_point(self):
        diff = Point()
        self.assertNotEqual(self.point, diff)

    def test_with_overwritten_value(self):
        diff = Point(self.point, a = 3)
        self.assertNotEqual(self.point, diff)

    def test_with_additional_axis(self):
        diff = Point(self.point, b = 3)
        self.assertNotEqual(self.point, diff)

    def test_with_additional_axis_sorted_last(self):
        diff = Point(self.point, z = 4)
        self.assertNotEqual(self.point, diff)


class PointIsSameSpaceTests(unittest.TestCase):
    def setUp(self):
        self.point = Point(x = 1, y = 2, z = 3)

    def test_with_same(self):
        same = Point(self.point)
        self.assertTrue(same.is_same_space(self.point))

    def test_with_different(self):
        diff = Point(self.point, t = 3)
        self.assertFalse(diff.is_same_space(self.point))


class PointsAdditionTests(unittest.TestCase):
    def setUp(self):
        self.point = Point(x = 1, y = 2)

    def test_correct_input(self):
        b = self.point + self.point
        self.assertNotEqual(self.point, b)
        self.assertEqual(b.x, 2)
        self.assertEqual(b.y, 4)

    def test_different_axes(self):
        b = Point(a = 1, b = 2)
        with self.assertRaises(AxesError, msg='Given points with different axes should raise AxesError.'):
            c = b + self.point

    def test_additional_axes(self):
        b = Point(self.point, z = 3)
        with self.assertRaises(AxesError, msg='Given points with different amount of axes should raise AxesError'):
            c = b + self.point


class PointsSubtractionTests(unittest.TestCase):
    def setUp(self):
        self.point = Point(x = 1, y = 2)

    def test_correct_input(self):
        b = self.point - self.point
        self.assertNotEqual(self.point, b)
        self.assertEqual(b.x, 0)
        self.assertEqual(b.y, 0)

    def test_different_axes(self):
        b = Point(a = 1, b = 2)
        with self.assertRaises(AxesError, msg='Given points with different axes should raise AxesError.'):
            c = b - self.point

    def test_additional_axes(self):
        b = Point(self.point, z = 3)
        with self.assertRaises(AxesError, msg='Given points with different amount of axes should raise AxesError'):
            c = b - self.point


class PointDistanceToTests(unittest.TestCase):
    def setUp(self):
        self.point = Point(x = 2, y = 4)

    def test_correct_input(self):
        b = Point(self.point, x = 4)
        self.assertEqual(b.distance_to(self.point), 2)

    def test_axes_erroneous_input(self):
        b = Point(self.point, z = 3)
        with self.assertRaises(AxesError, msg='Given points with different axes should raise AxesError.'):
            self.point.distance_to(b)


class PointOriginTest(unittest.TestCase):
    def runTest(self):
        a = Point(x = 1, y = 2, z = 4)
        b = a.origin()
        for axis in b.axes:
            self.assertEqual(b._Point__axes[axis], 0)
