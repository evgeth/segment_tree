class Operation:
    def __init__(self, name, function, function_on_equal, neutral_value=0):
        self.name = name
        self.f = function
        self.f_on_equal = function_on_equal


def add_multiple(x, count):
    return x * count


def min_multiple(x, count):
    return x


def max_multiple(x, count):
    return x


sum_operation = Operation("sum", sum, add_multiple, 0)
min_operation = Operation("min", min, min_multiple, 1e9)
max_operation = Operation("max", max, max_multiple, -1e9)
