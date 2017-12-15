# Segment Tree with range operations

![LicenseLink](https://img.shields.io/badge/license-MIT-blue.svg)

This is a general implementation of a segment tree for Python 3.

* Semigroup range operations in O(logN) time
* Built-in support for `max`, `min`, `sum` operations
* Extensible to support more semigroup operations
* Limited support for multidimensional trees
* Python 2 is not currently supported

Installation
============
`pip3 install segment-tree`

Segment Tree (one-dimensional)
============
## Basic usage
```python

    from segment_tree import *
    array = [3, 1, 5, 3, 13, 7, 2, 7, 2]
    tree = SegmentTree(array)

    t.query(1, 3, "sum") # 9
    t.update(0, 10) # [10, 1, 5, 3, 13, 7, 2, 7, 2]
    t.query(0, 8, "min") # 0
    t.update(2, -1) # [10, 1, -1, 3, 13, 7, 2, 0, 2]
    t.query(0, 2, "min") # -1
```
## Updates on ranges
```python
    from segment_tree import *
    array = [1, 2, 3, 4, 5]
    t = SegmentTree(array)
    t.update_range(0, 2, 6) # 6 6 6 4 5
    t.update_range(1, 4, 2) # 6 2 2 2 2
    t.query(0, 3, "min") # 2
```

## Operations and their complexity
`n` is total number of elements in the array.

| Function | Description | Complexity | Additional storage
| ------ |---------|----------:|------:
| `SegmentTree(array)` | Builds a segment tree from an `array` | O(n) | O(n)        
| `update(position, value)` | Updates an old value at `position` to `value`| O(log n) | O(1)
| `update_range(start, end, value)` | Sets `value` on a `[start, end]` range | O(log n) | O(1)
| `query(start, end, function)` | Returns `function([start, end])`| O(log n) | O(1)


Multidimensional Segment Tree (alpha version, might have bugs)
============
## Basic usage
```python
    from segment_tree import *
    a = [[[1, 2], [1, 3]], [[-1, -2], [-1, -3]]]
    tree = MultidimensionalSegmentTree(a)

    tree.query([(0, 1), (0, 0), (0, 0)], max) # 1
    tree.query([(1, 1), (0, 1), (0, 1)], sum) # -7
    tree.query([(0, 1), (1, 1), (0, 1)], min) # -3
```

## Operations and their complexity
`n` is total number of elements in the array, `p` is the number of dimensions.

| Function | Description | Complexity | Additional storage
| ------ |---------|----------:|------:
| `MultidimensionalSegmentTree(array)` | Builds a multidimensional segment tree from an `array` | O(4^p * n) | O(4^p * n)        
| `update(position, value)` (not implemented yet) | Updates an old value at `position` to `value`| O(log^p n) | O(1)
| `query(start, end, function)` | Returns `function([start, end])`| O(log^p n) | O(1)

Tests
=====
Execute `python3 setup.py test` to run tests.
