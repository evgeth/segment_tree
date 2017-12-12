from segment_tree.operations import *

class SegmentTree:
    def __init__(self, array, functions=[min, max, add, mul]):
        self.array = array
        self.functions = functions
        self.root = SegmentTreeNode(0, len(array) - 1, self)

    def query(self, start, end, function):
        if function not in self.functions:
            raise NotImplemented
        return self.root.query(start, end, function)

    def summary(self):
        return self.root.values

    def update(self, position, value):
        self.root.update(position, value)

    def add(self, start, end, value):
        self.root.add(start, end, value)

    def __repr__(self):
        return self.root.__repr__()


class SegmentTreeNode:
    def __init__(self, start, end, segment_tree):
        self.range = (start, end)
        self.parent_tree = segment_tree
        self.values = {}
        self.left = None
        self.right = None
        if start == end:
            self.sync()
            return
        self.left = SegmentTreeNode(start, start + (end - start) // 2, segment_tree)
        self.right = SegmentTreeNode(start + (end - start) // 2 + 1, end, segment_tree)
        self.sync()


    def query(self, start, end, function):
        if end < self.range[0] or start > self.range[1]:
            return None
        if start <= self.range[0] and self.range[1] <= end:
            return self.values[function.__name__]
        left_res = self.left.query(start, end, function) if self.left else None
        right_res = self.right.query(start, end, function) if self.right else None
        if left_res is None:
            return right_res
        if right_res is None:
            return left_res
        return function(left_res, right_res)

    def update(self, position, value):
        if position < self.range[0] or position > self.range[1]:
            return
        if position == self.range[0] and self.range[1] == position:
            self.parent_tree.array[position] = value
            self.sync()
            return
        self.left.update(position, value)
        self.right.update(position, value)
        self.sync()


    def sync(self):
        if self.range[0] == self.range[1]:
            for function in self.parent_tree.functions:
                self.values[function.__name__] = self.parent_tree.array[self.range[0]]
        else:
            for function in self.parent_tree.functions:
                self.values[function.__name__] = function(self.left.values[function.__name__],
                                                          self.right.values[function.__name__])

    def __repr__(self):
        ans = "({}, {}): {}\n".format(self.range[0], self.range[1], self.values)
        if self.left:
            ans += self.left.__repr__()
        if self.right:
            ans += self.right.__repr__()
        return ans
