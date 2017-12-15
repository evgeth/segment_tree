from segment_tree.operations import *

class NaiveSegmentTree:
    def __init__(self, array, operations=[sum_operation, min_operation, max_operation]):
        self.array = array
        self.operations = {}
        for op in operations:
            self.operations[op.name] = op

    def query(self, start, end, operation_name):
        if self.operations.get(operation_name) == None:
            raise Exception("This operation is not available")
        op = self.operations[operation_name]
        return op.f(self.array[start:end + 1])

    def summary(self):
        return self.root.values

    def update(self, position, value):
        self.array[position] = value

    def add(self, start, end, value):
        for i in range(start, end + 1):
            self.array[i] += value

    def __repr__(self):
        return self.root.__repr__()
