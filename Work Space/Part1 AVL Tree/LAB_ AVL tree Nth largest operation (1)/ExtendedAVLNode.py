from AVLNode import AVLNode

class ExtendedAVLNode(AVLNode):
    # Initializes the ExtendedAVLNode with the given key
    # and sets subtree_key_count to 1.
    def __init__(self, node_key):
        super().__init__(node_key)
        self.subtree_key_count = 1

    # Returns the count of keys in the subtree rooted at this node.
    def get_subtree_key_count(self):
        return self.subtree_key_count

    # Updates the count of keys in the subtree rooted at this node.
    def update_subtree_key_count(self):
        self.subtree_key_count = 1 + self.get_left_subtree_key_count() + self.get_right_subtree_key_count()

    # Returns the count of keys in the left subtree.
    def get_left_subtree_key_count(self):
        return self.get_left().get_subtree_key_count() if self.get_left() else 0

    # Returns the count of keys in the right subtree.
    def get_right_subtree_key_count(self):
        return self.get_right().get_subtree_key_count() if self.get_right() else 0
