import numpy as np


class MultidimensionalSegmentTree:
    """
    Implementation of a multidimensional segment tree. Alpha version, might
    contain bugs. Does not support range updates yet.
    """

    def __init__(self, array, functions=[min, max, sum], dimensions=1):
        """
        Builds a segment tree based on the provided `array`. `array` can have
        arbitrary number of dimensions.
        """
        self.array = np.asarray(array)
        self.nodes = {}
        self.dimensions = len(self.array.shape)
        if type(functions) != list:
            raise TypeError("functions must be a list")
        self.functions = functions
        node_range = []
        for i in range(len(self.array.shape)):
            node_range.append((0, self.array.shape[i] - 1))
        node_range = tuple(node_range)
        self.nodes[node_range] = MSegmentTreeNode(tuple(node_range), self)
        self.root = self.nodes[node_range]

    def query(self, query_range, function):
        """
        Returns the result of the function
        on the query range.
        `query_range` is a list of tuples, where each tuple indicates the bounds
        in particular dimension.
        """
        if function not in self.functions:
            raise NotImplemented
        return self.root.query(query_range, function)

    def summary(self):
        """
        Prints the summary for the whole array (values in the root node).
        """
        return self.root.values

    def __repr__(self):
        return self.root.__repr__()


class MSegmentTreeNode:
    def __init__(self, node_range, segment_tree):
        if segment_tree.nodes.get(node_range) != None:
            return
        self.range = node_range
        self.parent_tree = segment_tree
        self.values = {}
        self.left = None
        self.right = None
        segment_tree.nodes[node_range] = self
        self.dimension = None
        for i in range(len(list(self.range))):
            if self.range[i][0] != self.range[i][1]:
                left_subtree_range = list(self.range)
                right_subtree_range = list(self.range)
                start = self.range[i][0]
                end = self.range[i][1]
                left_subtree_range[i] = (start, start + (end - start) // 2)
                right_subtree_range[i] = (start + (end - start) // 2 + 1, end)
                l = MSegmentTreeNode(tuple(left_subtree_range), segment_tree)
                if self.dimension is None:
                    self.left = l
                r = MSegmentTreeNode(tuple(right_subtree_range), segment_tree)
                if self.dimension is None:
                    self.right = r
                if self.dimension is None:
                    for function in self.parent_tree.functions:
                        self.values[function.__name__] = function([
                            self.left.values[function.__name__],
                            self.right.values[function.__name__]
                        ])
                self.dimension = i
                break
        if self.dimension is None:
            index = tuple([i for i, j in self.range])
            for function in self.parent_tree.functions:
                self.values[function.__name__] = function(
                    [self.parent_tree.array[index]])

    def query(self, query_range, function, dimension=0):
        start = query_range[dimension][0]
        end = query_range[dimension][1]
        l_bound = list(self.range)[dimension][0]
        r_bound = list(self.range)[dimension][1]
        if end < l_bound or start > r_bound:
            return None
        if start <= l_bound and r_bound <= end:
            if dimension == self.parent_tree.dimensions - 1:
                return self.values[function.__name__]
            else:
                return self.query(query_range, function, dimension + 1)
        left_res = self.left.query(query_range, function,
                                   dimension) if self.left else None
        right_res = self.right.query(query_range, function,
                                     dimension) if self.right else None

        if left_res is None:
            return right_res
        if right_res is None:
            return left_res
        return function([left_res, right_res])
