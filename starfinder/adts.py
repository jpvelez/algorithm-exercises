import numpy as np

def distance(point1, point2):
    '''
    Compute distance between points p and q in Euclidean
    space, represented as n-dimensional Euclidean vectors.

    Use numpy array for performance and clarity.
    '''
    q = np.array(point1)
    p = np.array(point2)
    return np.sqrt(np.sum((q - p) ** 2))

class KDTree:
    '''
    K-dimensional tree implementation, a type of binary space
    partitioning tree for doing nearest neighbor searches.
    '''

    def __init__(self, point_list):
        # Dimensionality of space the tree is partitioning.
        self.d = len(point_list[0])
        # Build tree and save reference to root.
        self.root = self.build(point_list, 0)

    class Node():
        '''
        Constructor for binary tree node.
        '''
        def __init__(self):
            self.point = None  # Multidimensional node key.
            self.attr = None   # Info associated with point.
            self.left = None
            self.right = None

    def build(self, point_list, level):
        '''
        Build KDTree from list of k-d points.
        Elements in point list should be a tuple representing
        a k-dimensional point, and an arbitrary object associated
        with that point.
        [((15.6, -197.0, 25.1, ..), {'foo': 'bar'..}) ..]
        '''
        # Base case: no more points in the list means we
        # have arrived at leaf node.
        if len(point_list) == 0:
            return None

        # Change axis we split on at each level of the tree.
        axis = level % self.d

        # Find median value of axis to split on.
        sorted_points = sorted(point_list, key=lambda point: point[0][axis])
        median_ix = int(len(point_list) / 2)

        # Build a new tree, store median point in the root node.
        root = self.Node()
        point, attr = sorted_points[median_ix]
        root.point = point
        root.attr = attr  # Additional point data.

        # Recursively construct subtrees on either side of split.
        # Store points lesser than median (along current axis) in left subtree.
        root.left = self.build(sorted_points[:median_ix], level + 1)
        # Store points greater than median (along current axis) in right subtree.
        root.right = self.build(sorted_points[median_ix + 1:], level + 1)
        return root

    def find_k_nearest_neighbors(self, search_point, k):
        '''
        Find k nearest neighbors to client-supplied search point.
        Returns a BoundedPriorityQueue that can be iterated through
        for nearest neighbors.
        '''
        self.search_point = search_point
        self.bpq = BoundedPriorityQueue(k)
        self.knn(self.root, level=0)
        return self.bpq

    def knn(self, current_node, level):
        '''
        K nearest neighbors algorithm. Performs recursive
        search on KDTree, using a BoundedPriorityQueue to keep
        track of K nearest neighbors.
        '''
        # Change axis we split on at each level of the tree.
        axis = level % self.d
        a = self.search_point[axis]  # Value of search point on current dimension.

        ################
        # WALKING DOWN #
        ################
        # Walk down the tree recursively, as if you were looking for
        # the search point in the tree, until you reach a tree leaf.
        # Save that node point as the "best guess node."

        # Base case: tree leaf reached.
        if current_node is None:
            return

        # Descend left or right subtree, on whether search point is greater than
        # or less than current node point on the current axis. Equivalent to
        # picking the region of space created by the current point's splitting
        # hyperplane that search point is in.
        if a < current_node.point[axis]:
            self.knn(current_node.left, level + 1)
        else:
            self.knn(current_node.right, level + 1)

        ##############
        # WALKING UP #
        ##############
        # After recursion bottoms out, walk back up the tree.
        # Attempt to insert node into bounded priority queue.
        # If queue is full, it will only be kept if it is closer than the
        # kth closest point we've seen so far.
        distance_to_point = distance(current_node.point, self.search_point)
        self.bpq.enqueue(distance_to_point, current_node.attr)

        # Walk back up the tree, check whether candidate hypersphere
        # created by our current "lowest priority" / largest distance
        # best guess node crosses splitting hyperplane of current node.
        # Also, check is the queue is not full yet.
        kth_largest_distance = self.bpq.lowest_priority_item().key
        if self.bpq.size < self.bpq.max_elements \
           or abs(current_node.point[axis] - a) < kth_largest_distance:
            # If so, check other side of the tree to see if there are
            # closer points than our best guess.
            if a < current_node.point[axis]:
                self.knn(current_node.right, level + 1)
            else:
                self.knn(current_node.left, level + 1)
            # If not, continue to unwind the recursion, implicitly
            # eliminating all other points from the splitting hyperplane.

class PriorityQueue():

    def __init__(self, k):
        # Data structure: complete heap-ordered binary tree,
        # represented in array.
        self.heap = [0] # 1st element empty so we can order array by tree level.
        self.size = 0
        self.max_size = k

    ##################
    # Helper methods #
    ##################
    def swap(self, ix, parent_ix):
        '''Exchange a node with its parent in the heap.'''
        temp_node = self.heap[ix]
        self.heap[ix] = self.heap[parent_ix]
        self.heap[parent_ix] = temp_node

    def less_than(self, a, b):
        return self.compare(a, b) < 0

    def more_than(self, a, b):
        return self.compare(a, b) > 0

    def compare(self, a, b):
        '''
        Compare the keys of nodes living at index a and b
        of the heap.
        '''
        if self.heap[a]['key'] < self.heap[b]['key']:
            return -1
        elif self.heap[a]['key'] > self.heap[b]['key']:
            return 1
        else:
            return 0

    ################
    # Heap methods #
    ################
    def sink(self, ix):
        while (ix * 2) <= self.size:
            min_child_ix = self.find_min_child(ix)
            if self.more_than(ix, min_child_ix):
                self.swap(ix, min_child_ix)
            ix = min_child_ix

    def find_min_child(self, ix):
        '''
        Find child of node at index ix that has
        the minimum key value. Returns index of
        that child.
        '''
        left_child_ix = ix * 2
        right_child_ix = ix * 2 + 1
        # If node only has left child, because right
        # child is at end of the array, avoid IndexError.
        if right_child_ix > self.size:
            return left_child_ix
        else:
            if self.less_than(left_child_ix, right_child_ix):
                return left_child_ix
            else:
                return right_child_ix

    def swim(self, ix):
        # The children of a node at index p, if any, are stored
        # at 2p and 2p+1. Given a node, then, we can use integer
        # division to find its parent.
        parent_ix = ix // 2
        # Compare key to parents in each level in the tree.
        while parent_ix > 0:
            if self.less_than(ix, parent_ix):
                self.swap(ix, parent_ix)
        ix = parent_ix


    #####################
    # PriorityQueue API #
    #####################
    def push(self, key, value):
        '''Insert operation.'''
        self.heap.append({'key': key, 'value': value})
        self.size += 1
        self.swim(self.size)  # Try to percolate value up the heap.

    def pop(self):
        '''Get min value operation.'''
        # Remove root, replace it with last inserted node.
        key, value = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        # Restore heap-ordered property of the tree.
        self.sink(1)
        return key, value


class BoundedPriorityQueue():
    '''
    Bounded Priority Queue ADT. Keeps track
    of k minimum elements that are inserted into it.
    '''

    def __init__(self, k):
        self.max_elements = k
        self.head = None
        self.size = 0

    ##################
    # Helper methods #
    ##################
    class Node():
        '''Node for linked list.'''
        def __init__(self):
            self.key = None
            self.value = None
            self.next = None

    def _build_node(self, key, value):
        node = self.Node()
        node.key = key
        node.value = value
        return node

    def _pop(self):
        '''Remove node from the tail of the list.'''
        current = self.head
        # Traverse the list.
        while current is not None:
            # If next value is the list tail, remove it.
            if current.next.next is None:
                current.next = None
            current = current.next

    def __iter__(self):
        '''Make Priority Queue iterable.'''
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def lowest_priority_item(self):
        '''
        Return the lowest priority item in the queue. If queue
        is full, this is the kth highest priority item inserted
        into the queue so far.
        '''
        current = self.head
        while current.next is not None:
            current = current.next
        return current

    #####################
    # PriorityQueue API #
    #####################
    def enqueue(self, key, value):
        # Make new node.
        node = self._build_node(key, value)
        self.size += 1

        # If list is empty, make node the head.
        if self.head is None:
            self.head = node
            self.tail = node

        # If key is smaller than head, prepend note to list.
        elif key < self.head.key:
            old_head = self.head
            self.head = node
            self.head.next = old_head

        # If list ends after current, insert yourself at the end.
        # If not, check if you're smaller than the node after current,
        # and insert yourself in between them if you are.
        # If you aren't, traverse to the next node.
        else:
            current = self.head
            while current.next is not None:
                if key < current.next.key:
                    break
                current = current.next
            node.next = current.next
            current.next = node

        # Keep the list bounded to min k elements.
        if self.size > self.max_elements:
            self._pop()

    def dequeue(self):
        min_node = self.head
        self.head = min_node.next
        self.size -= 1
        return min_node.key, min_node.value
