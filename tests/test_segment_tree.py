from unittest import TestCase

from segment_tree import *

class TestSegmentTree(TestCase):
    def test_simple(self):
        array = [3, 1, 5, 3, 13, 7, 2, 7, 2]
        t = SegmentTree(array)

        self.assertEqual(t.query(1, 3, add), 5)
        t.update(0, 10) # [10, 1, 5, 3, 13, 7, 2, 7, 2]
        self.assertEqual(t.query(0, 3, add), 19)
        t.update(7, 0) # [10, 1, 5, 3, 13, 7, 2, 0, 2]
        self.assertEqual(t.query(0, 8, min), 0)
        t.update(2, -1) # [10, 1, -1, 3, 13, 7, 2, 0, 2]
        self.assertEqual(t.query(0, 2, min), -1)
