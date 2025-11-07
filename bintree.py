import pickle
from nodes import Node

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, vehicle):
        def _insert(node, vehicle):
            if node is None:
                return Node(vehicle)
            if vehicle.performance() < node.vehicle.performance():
                node.left = _insert(node.left, vehicle)
            else:
                node.right = _insert(node.right, vehicle)
            return node
        self.root = _insert(self.root, vehicle)

    def inorder_traversal(self):
        def _inorder(node):
            if node:
                yield from _inorder(node.left)
                yield node.vehicle
                yield from _inorder(node.right)
        yield from _inorder(self.root)

    def find_by_model(self, model):
        def _search(node, model):
            if node is None:
                return None
            if node.vehicle.model == model:
                return node.vehicle
            left = _search(node.left, model)
            return left if left else _search(node.right, model)
        return _search(self.root, model)

    def filter_by_performance(self, threshold):
        return [v for v in self.inorder_traversal() if v.performance() > threshold]

    def __iter__(self):
        return self.inorder_traversal()

    def serialize(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.root, f)

    def deserialize(self, filename):
        with open(filename, 'rb') as f:
            self.root = pickle.load(f)
