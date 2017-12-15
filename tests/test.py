from unittest import TestCase

from segment_tree import *
from tests.naive_segment_tree import *
import random


class TestSegmentTree(TestCase):
    def test_int_segment_tree(self):
        """
        Tests a basic implementation of the segment tree with integer values.
        """
        array_length = 100
        number_of_queries = 100
        array = [random.randint(-100, 100) for i in range(array_length)]
        t = SegmentTree(array)
        test_t = NaiveSegmentTree(array)

        for i in range(number_of_queries):
            l = random.randint(0, array_length - 1)
            r = random.randint(l, array_length - 1)
            self.assertEqual(t.query(l, r, "min"), test_t.query(l, r, "min"))
            self.assertEqual(t.query(l, r, "max"), test_t.query(l, r, "max"))
            self.assertEqual(t.query(l, r, "sum"), test_t.query(l, r, "sum"))

    def test_float_segment_tree(self):
        """
        Tests a basic implementation of the segment tree with float values.
        """
        array_length = 100
        number_of_queries = 100
        array = [random.random() for i in range(array_length)]
        t = SegmentTree(array)
        test_t = NaiveSegmentTree(array)

        for i in range(number_of_queries):
            l = random.randint(0, array_length - 1)
            r = random.randint(l, array_length - 1)
            self.assertAlmostEqual(
                t.query(l, r, "min"), test_t.query(l, r, "min"))
            self.assertAlmostEqual(
                t.query(l, r, "max"), test_t.query(l, r, "max"))
            self.assertAlmostEqual(
                t.query(l, r, "sum"), test_t.query(l, r, "sum"))

    def test_updates_of_values(self):
        """
        Tests a basic implementation of the segment tree with tree updates.
        """
        array_length = 100
        number_of_queries = 500
        array = [random.randint(-100, 100) for i in range(array_length)]
        t = SegmentTree(array)
        test_t = NaiveSegmentTree(array[:])

        for i in range(number_of_queries):
            update_pos = random.randint(0, array_length - 1)
            new_value = random.randint(-100, 100)
            t.update(update_pos, new_value)
            test_t.update(update_pos, new_value)
            l = random.randint(0, update_pos)
            r = random.randint(update_pos, array_length - 1)
            self.assertEqual(t.query(l, r, "min"), test_t.query(l, r, "min"))
            self.assertEqual(t.query(l, r, "max"), test_t.query(l, r, "max"))
            self.assertEqual(t.query(l, r, "sum"), test_t.query(l, r, "sum"))

    def test_updates_on_ranges(self):
        """
        Tests a basic implementation of the segment tree with updates on ranges.
        """
        array_length = 100
        number_of_queries = 500
        array = [random.randint(-100, 100) for i in range(array_length)]
        t = SegmentTree(array)
        test_array = array[:]
        test_t = NaiveSegmentTree(test_array)
        for i in range(number_of_queries):
            update_l = random.randint(0, array_length - 1)
            update_r = random.randint(update_l, array_length - 1)
            new_value = random.randint(-100, 100)
            t.update_range(update_l, update_r, new_value)
            test_t.update_range(update_l, update_r, new_value)
            l = random.randint(0, update_l)
            r = random.randint(update_r, array_length - 1)
            self.assertEqual(t.query(l, r, "min"), test_t.query(l, r, "min"))
            self.assertEqual(t.query(l, r, "max"), test_t.query(l, r, "max"))
            self.assertEqual(t.query(l, r, "sum"), test_t.query(l, r, "sum"))
