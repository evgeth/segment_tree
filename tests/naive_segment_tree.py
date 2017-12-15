from segment_tree.operations import *

class NaiveSegmentTree:
    def __init__(self, array, functions=[min, max, sum]):
        self.array = array
        self.functions = functions

    def query(self, start, end, function):
        if function not in self.functions:
            raise NotImplemented
        return function(self.array[start:end + 1])

    def summary(self):
        return self.root.values

    def update(self, position, value):
        self.array[position] = value

    def add(self, start, end, value):
        for i in range(start, end + 1):
            self.array[i] += value

    def __repr__(self):
        return self.root.__repr__()
