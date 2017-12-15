from segment_tree.operations import *

class SegmentTree:
    def __init__(self, array, operations=[sum_operation, min_operation, max_operation]):
        self.array = array
        if type(operations) != list:
            raise TypeError("operations must be a list")
        self.operations = {}
        for op in operations:
            self.operations[op.name] = op
        self.root = SegmentTreeNode(0, len(array) - 1, self)

    def query(self, start, end, operation_name):
        if self.operations.get(operation_name) == None:
            raise Exception("This operation is not available")
        return self.root.query(start, end, self.operations[operation_name])

    def summary(self):
        return self.root.values

    def update(self, position, value):
        self.root.update(position, value)

    def update_range(self, start, end, value):
        self.root.update_range(start, end, value)

    def __repr__(self):
        return self.root.__repr__()


class SegmentTreeNode:
    def __init__(self, start, end, segment_tree):
        self.range = (start, end)
        self.parent_tree = segment_tree
        self.range_value = None
        self.values = {}
        self.left = None
        self.right = None
        if start == end:
            self.sync()
            return
        self.left = SegmentTreeNode(start, start + (end - start) // 2, segment_tree)
        self.right = SegmentTreeNode(start + (end - start) // 2 + 1, end, segment_tree)
        self.sync()


    def query(self, start, end, operation):
        if end < self.range[0] or start > self.range[1]:
            return None
        if start <= self.range[0] and self.range[1] <= end:
            return self.values[operation.name]
        self.push()
        left_res = self.left.query(start, end, operation) if self.left else None
        right_res = self.right.query(start, end, operation) if self.right else None
        if left_res is None:
            return right_res
        if right_res is None:
            return left_res
        return operation.f([left_res, right_res])

    def update(self, position, value):
        if position < self.range[0] or position > self.range[1]:
            return
        if position == self.range[0] and self.range[1] == position:
            self.parent_tree.array[position] = value
            self.sync()
            return
        self.push()
        self.left.update(position, value)
        self.right.update(position, value)
        self.sync()

    def update_range(self, start, end, value):
        if end < self.range[0] or start > self.range[1]:
            return
        if start <= self.range[0] and self.range[1] <= end:
            self.range_value = value
            self.sync()
            return
        self.push()
        self.left.update_range(start, end, value)
        self.right.update_range(start, end, value)
        self.sync()

    def sync(self):
        if self.range[0] == self.range[1]:
            for op in self.parent_tree.operations.values():
                current_value = self.parent_tree.array[self.range[0]]
                if self.range_value is not None:
                    current_value = self.range_value
                self.values[op.name] = op.f([current_value])
        else:
            for op in self.parent_tree.operations.values():
                result = op.f([self.left.values[op.name],
                               self.right.values[op.name]])
                if self.range_value is not None:
                    bound_length = self.range[1] - self.range[0] + 1
                    result = op.f_on_equal(self.range_value, bound_length)
                self.values[op.name] = result

    def push(self):
        if self.range_value is None:
            return
        if self.left:
            self.left.range_value = self.range_value
            self.right.range_value = self.range_value
            self.left.sync()
            self.right.sync()
            self.range_value = None

    def __repr__(self):
        ans = "({}, {}): {}\n".format(self.range[0], self.range[1], self.values)
        if self.left:
            ans += self.left.__repr__()
        if self.right:
            ans += self.right.__repr__()
        return ans
