from AVLTree import AVLTree
from ExtendedAVLNode import ExtendedAVLNode

class ExtendedAVLTree(AVLTree):
    def __init__(self):
        super().__init__()

    # each node in an ExtendedAVLTree is an ExtendedAVLNode.
    def make_new_node(self, key):
        return ExtendedAVLNode(key)

    # Type additional code here.

    def get_nth_key(self, n):
        # Type your code here.
        
        return 0
