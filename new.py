WARNING: Attempting to work in a virtualenv. If you encounter problems, please install IPython inside the virtualenv.
Python 3.4.4 |Anaconda 2.3.0 (x86_64)| (default, Jan  9 2016, 17:30:09) 
Type "copyright", "credits" or "license" for more information.

IPython 3.2.0 -- An enhanced Interactive Python.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://anaconda.org
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: 
In [2]: 
In [3]: 
In [4]: import numpy

In [5]: q = (0, 0)

In [9]: p = (1, 1)

In [10]: (q[0] + p[0])**2
Out[17]: 1

In [18]: (q[0] + p[0])**2 + (q[1] + p[1])**2
Out[18]: 2

In [19]: sqrt(2)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-19-40e415486bd6> in <module>()
----> 1 sqrt(2)

NameError: name 'sqrt' is not defined

In [20]: import math

In [26]: math.sqrt((q[0] + p[0])**2 + (q[1] + p[1])**2)
Out[29]: 1.4142135623730951

In [30]: d = math.sqrt((q[0] + p[0])**2 + (q[1] + p[1])**2)

In [34]: import numpy as np

In [36]: np.array(p)
Out[44]: array([1, 1])

In [45]: np.array(q) + np.array(p)
Out[50]: array([1, 1])

In [51]: np.array(q) - np.array(p)
Out[51]: array([-1, -1])

In [52]: q = np.array(q)

In [54]: p = np.array(p)

In [55]: p
Out[55]: array([1, 1])

In [56]: q
Out[56]: array([0, 0])

In [57]: (q - p)
Out[58]: array([-1, -1])

In [59]: (q - p)**2
Out[59]: array([1, 1])

In [60]: sum((q - p)**2)
Out[60]: 2

In [61]: np.sum((q - p)**2)
Out[61]: 2

In [62]: ((q - p)**2).sum()
Out[67]: 2

In [68]: ((q - p)**2).sum(axis=0)
Out[71]: 2

In [72]: ((q - p)**2).sum(axis=1)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-72-fa981463d3d5> in <module>()
----> 1 ((q - p)**2).sum(axis=1)

/Users/jpvelez/anaconda/lib/python3.4/site-packages/numpy/core/_methods.py in _sum(a, axis, dtype, out, keepdims)
     30 
     31 def _sum(a, axis=None, dtype=None, out=None, keepdims=False):
---> 32     return umr_sum(a, axis, dtype, out, keepdims)
     33 
     34 def _prod(a, axis=None, dtype=None, out=None, keepdims=False):

ValueError: 'axis' entry is out of bounds

In [73]: ((q - p)**2).sum()
Out[73]: 2

In [74]: np.sqrt(((q - p)**2).sum())
Out[74]: 1.4142135623730951

In [75]: np.sqrt(np.square(q - p).sum())
Out[76]: 1.4142135623730951

In [77]: np.sqrt(np.sum(np.square(q - p)))
Out[77]: 1.4142135623730951

In [78]: (q - p).square()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-81-1ebe22c38fb2> in <module>()
----> 1 (q - p).square()

AttributeError: 'numpy.ndarray' object has no attribute 'square'

In [82]: (q - p) ** 2
Out[82]: array([1, 1])

In [83]: np.sum((q - p) ** 2)
Out[87]: 2

In [88]: np.sqrt(np.sum((q - p) ** 2))
Out[88]: 1.4142135623730951

In [89]: range(0,10)
Out[93]: range(0, 10)

In [94]: sorted(range(0,10))
Out[94]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [95]: sorted(range(0,10))[:5]
Out[95]: [0, 1, 2, 3, 4]

In [96]:   File "/Users/jpvelez/src/nyt/new.py", line 2
    class None:
             ^
SyntaxError: invalid syntax


In [97]:   File "/Users/jpvelez/src/nyt/new.py", line 2
    class None():
             ^
SyntaxError: invalid syntax


In [98]: 
In [99]: n = Node()

In [101]: n.value

In [104]: n.value = foo
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-104-92594bcbb4f7> in <module>()
----> 1 n.value = foo

NameError: name 'foo' is not defined

In [105]: n.value = foo
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-106-92594bcbb4f7> in <module>()
----> 1 n.value = foo

NameError: name 'foo' is not defined

In [107]: n.value = ''foo'
  File "<ipython-input-107-cd43bd0fcea5>", line 1
    n.value = ''foo'
                  ^
SyntaxError: invalid syntax


In [108]: n.value = 'foo'

In [109]: n.value
Out[109]: 'foo'

In [110]: 10 < None
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-110-e319aa63991f> in <module>()
----> 1 10 < None

TypeError: unorderable types: int() < NoneType()

In [111]: 10 < inf
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-114-23509cfd824f> in <module>()
----> 1 10 < inf

NameError: name 'inf' is not defined

In [115]: 10 < Inf
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-115-c89dd182e9f4> in <module>()
----> 1 10 < Inf

NameError: name 'Inf' is not defined

In [116]: 10 < float('inf')
Out[116]: True

In [117]: int('inf')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-117-688290731b67> in <module>()
----> 1 int('inf')

ValueError: invalid literal for int() with base 10: 'inf'

In [118]: 
In [119]: 
In [120]: tree = KDTree()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-121-af69e818ea58> in <module>()
----> 1 tree = KDTree()

TypeError: __init__() missing 1 required positional argument: 'point_list'

In [122]: point_list = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)]

In [126]: tree = KDTree(point_list)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-126-345f917190b9> in <module>()
----> 1 tree = KDTree(point_list)

/Users/jpvelez/src/nyt/new.py in __init__(self, point_list)
      9 # TODO: MAKE THIS ALL A CLASS?
     10 class KDTree:
---> 11     '''TODO: Docstring.'''
     12 
     13     def __init__(self, point_list):

TypeError: build() got multiple values for argument 'level'

In [127]: 
In [128]: tree = KDTree(point_list)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-128-345f917190b9> in <module>()
----> 1 tree = KDTree(point_list)

/Users/jpvelez/src/nyt/new.py in __init__(self, point_list)
      9         self.k = len(point_list[0])
     10         # Build tree and save reference to root.
---> 11         self.root = self.build(point_list, level=0)
     12 
     13     class Node():

TypeError: build() got multiple values for argument 'level'

In [129]: 
In [130]: tree = KDTree(point_list)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-130-345f917190b9> in <module>()
----> 1 tree = KDTree(point_list)

/Users/jpvelez/src/nyt/new.py in __init__(self, point_list)
      9         self.k = len(point_list[0])
     10         # Build tree and save reference to root.
---> 11         self.root = self.build(point_list, level=0)
     12 
     13     class Node():

TypeError: build() got multiple values for argument 'level'

In [131]: 
In [132]: tree = KDTree(point_list)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-132-345f917190b9> in <module>()
----> 1 tree = KDTree(point_list)

/Users/jpvelez/src/nyt/new.py in __init__(self, point_list)
      9         self.k = len(point_list[0])
     10         # Build tree and save reference to root.
---> 11         self.root = self.build(point_list, 0)
     12 
     13     class Node():

TypeError: build() takes 2 positional arguments but 3 were given

In [133]: 
In [134]: tree = KDTree(point_list)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-134-345f917190b9> in <module>()
----> 1 tree = KDTree(point_list)

/Users/jpvelez/src/nyt/new.py in __init__(self, point_list)
      9         self.k = len(point_list[0])
     10         # Build tree and save reference to root.
---> 11         self.root = self.build(point_list, 0)
     12 
     13     class Node():

/Users/jpvelez/src/nyt/new.py in build(self, point_list, level)
     39         # Recursively construct subtrees on either side of split.
     40         # Points with values lesser than median (along current axis) are stored in left subtree.
---> 41         root.left = build_kdtree(sorted_points[:median_ix], level + 1)
     42         # Points with values greater than median are stored in right subtree.
     43         root.right = build_kdtree(sorted_points[median_ix + 1:], level + 1)

NameError: name 'build_kdtree' is not defined

In [135]: 
In [136]: tree = KDTree(point_list)

In [137]: tree.find_nearest_neighbors((0,0))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-141-91f88e91a58d> in <module>()
----> 1 tree.find_nearest_neighbors((0,0))

/Users/jpvelez/src/nyt/new.py in find_nearest_neighbors(self, search_point)
     52         self.best_guess_node = None
     53         self.best_guess_distance = float('inf')
---> 54         self.knn(self.root, level=0)
     55 
     56     def knn(self, current_node, level):

/Users/jpvelez/src/nyt/new.py in knn(self, current_node, level)
     74         # picking the region of space created by the current point's splitting
     75         # hyperplane that search point is in.
---> 76         if a < current_node[axis]:
     77             self.knn(current_node.left, level + 1)
     78         else:

TypeError: 'Node' object does not support indexing

In [142]: 
In [143]: tree = KDTree(point_list)

In [144]: tree.find_nearest_neighbors((0,0))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-144-91f88e91a58d> in <module>()
----> 1 tree.find_nearest_neighbors((0,0))

/Users/jpvelez/src/nyt/new.py in find_nearest_neighbors(self, search_point)
     52         self.best_guess_node = None
     53         self.best_guess_distance = float('inf')
---> 54         self.knn(self.root, level=0)
     55 
     56     def knn(self, current_node, level):

/Users/jpvelez/src/nyt/new.py in knn(self, current_node, level)
     74         # picking the region of space created by the current point's splitting
     75         # hyperplane that search point is in.
---> 76         if a < current_node[axis]:
     77             self.knn(current_node.left, level + 1)
     78         else:

TypeError: 'Node' object does not support indexing

In [145]: 
In [146]: tree = KDTree(point_list)

In [147]: tree.find_nearest_neighbors((0,0))
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-147-91f88e91a58d> in <module>()
----> 1 tree.find_nearest_neighbors((0,0))

/Users/jpvelez/src/nyt/new.py in find_nearest_neighbors(self, search_point)
     52         self.best_guess_node = None
     53         self.best_guess_distance = float('inf')
---> 54         self.knn(self.root, level=0)
     55 
     56     def knn(self, current_node, level):

/Users/jpvelez/src/nyt/new.py in knn(self, current_node, level)
     75         # hyperplane that search point is in.
     76         if a < current_node[axis]:
---> 77             self.knn(current_node.left, level + 1)
     78         else:
     79             self.knn(current_node.right, level + 1)

/Users/jpvelez/src/nyt/new.py in knn(self, current_node, level)
     75         # hyperplane that search point is in.
     76         if a < current_node[axis]:
---> 77             self.knn(current_node.left, level + 1)
     78         else:
     79             self.knn(current_node.right, level + 1)

/Users/jpvelez/src/nyt/new.py in knn(self, current_node, level)
     85         # closer to search point than best guess, make it the new best guess.
     86         distance_to_point = self.distance(current_node['point'], self.search_point)
---> 87         if distance_to_point < best_guess_distance:
     88             self.best_guess_node = current_node
     89             self.best_guess_distance = distance_to_point

NameError: name 'best_guess_distance' is not defined

In [148]: 
In [149]: tree = KDTree(point_list)

In [150]: tree.find_nearest_neighbors((0,0))

In [151]: 
In [152]: tree = KDTree(point_list)

In [153]: tree.find_nearest_neighbors((0,0))
Out[153]: <__main__.KDTree.Node at 0x1045f43c8>

In [154]: 
In [155]: tree = KDTree(point_list)

In [156]: nn = tree.find_nearest_neighbors((0,0))

In [157]: nn
Out[157]: (2, 3)

In [158]: 