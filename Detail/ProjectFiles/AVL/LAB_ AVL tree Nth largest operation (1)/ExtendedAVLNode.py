from AVLNode import AVLNode

class ExtendedAVLNode(AVLNode):

    def __init__(self, node_key):
        super().__init__(node_key)
        self.subtree_key_count = 1

    def get_subtree_key_count(self):
        return self.subtree_key_count

    # Type additional code here.
