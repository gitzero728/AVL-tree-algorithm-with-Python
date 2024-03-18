from AVLTree import AVLTree
from ExtendedAVLNode import ExtendedAVLNode

class ExtendedAVLTree(AVLTree):
    # Initializes the ExtendedAVLTree.
    def __init__(self):
        super().__init__()

    # Creates a new ExtendedAVLNode with the given key.
    def make_new_node(self, key):
        return ExtendedAVLNode(key)
    
    # Inserts a node into the tree and updates the subtree key counts.
    def insert_node(self, node):
        super().insert_node(node)
        self.update_all_subtree_key_counts()
    
    # Removes a node from the tree and updates the subtree key counts.
    def remove_node(self, node_to_remove):
        super().remove_node(node_to_remove)
        self.update_all_subtree_key_counts()

    # Updates the subtree key counts of all nodes in the tree.
    def update_all_subtree_key_counts(self):
        self.update_subtree_key_counts(self.root)

    # Updates the subtree key counts of a specific node in the tree.
    def update_subtree_key_counts(self, node):
        if node:
            self.update_subtree_key_counts(node.get_left())
            self.update_subtree_key_counts(node.get_right())
            node.update_subtree_key_count()

    # Returns the nth key of the tree.
    def get_nth_key(self, n):
        return self.get_nth_key_helper(self.root, n)

    # Helper method for get_nth_key.
    # Recursively finds the nth key in the tree.
    def get_nth_key_helper(self, node, n):
        if node is None:
            return None

        left_subtree_key_count = node.get_left_subtree_key_count()
        if n < left_subtree_key_count:
            return self.get_nth_key_helper(node.get_left(), n)
        elif n == left_subtree_key_count:
            return node.get_key()
        else:
            return self.get_nth_key_helper(node.get_right(), n - left_subtree_key_count - 1)
