Segment Tree implementation for Python 3
========================================

![LicenseLink](https://img.shields.io/badge/license-MIT-blue.svg)

This is a general implementation of a segment tree for Python 3.

* Semigroup range operations in O(logN) time
* Built-in support for `max`, `min`, `sum`, `mul` functions
* Extensible to support all semigroup operations
* Only Python 3 for now

Example usage
============

```python

    array = [3, 1, 5, 3, 13, 7, 2, 7, 2]
    tree = SegmentTree(array, [min, max, sum])

    t.query(1, 3, sum) # 9
    t.update(0, 10) # [10, 1, 5, 3, 13, 7, 2, 7, 2]
    t.query(0, 3, sum) # 19
    t.update(7, 0)  # [10, 1, 5, 3, 13, 7, 2, 0, 2]
    t.query(0, 8, min) # 0
    t.update(2, -1) # [10, 1, -1, 3, 13, 7, 2, 0, 2]
    t.query(0, 2, min) # -1
```

Installation
============
pip3 install segment-tree


Complexity of operations
============
TODO


Dependencies
============
TODO

Status: WIP
