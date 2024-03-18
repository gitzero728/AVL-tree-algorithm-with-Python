from BSTNode import BSTNode

class AVLNode(BSTNode):
    # Initializes the AVLNode with the given key. Height is assigned with 0.
    # super() sets left, right, and parent to None.
    def __init__(self, node_key):
        super().__init__(node_key)
        self.height = 0

    def get_left_height(self):
        left_child = self.get_left()
        return -1 if not left_child else left_child.height

    def get_right_height(self):
        right_child = self.get_right()
        return -1 if not right_child else right_child.height

    # Calculate this node's balance factor, defined as:
    # height(left subtree) - height(right subtree).
    def get_balance(self):
        # Get height of left and right subtrees.
        left_height = self.get_left_height()
        right_height = self.get_right_height()

        # Calculate the balance factor.
        return left_height - right_height

    def get_height(self):
        return self.height

    def get_left(self):
        return super().get_left()

    def get_right(self):
        return super().get_right()

    def set_left(self, new_left_child):
        # Call superclass's set_left() first.
        super().set_left(new_left_child)

        # Update height.
        self. update_height()

    def set_right(self, new_right_child):
        # Call superclass's set_right() first.
        super().set_right(new_right_child)

        # Update height.
        self. update_height()

    # Recalculate the current height of the subtree rooted at
    # the node, usually called after a subtree has been modified.
    def update_height(self):
        # Get height of left and right subtrees.
        left_height = self.get_left_height()
        right_height = self.get_right_height()

        # Assign height with 1 + the greater of the two.
        self.height = 1 + (left_height
                           if left_height > right_height
                           else right_height)
