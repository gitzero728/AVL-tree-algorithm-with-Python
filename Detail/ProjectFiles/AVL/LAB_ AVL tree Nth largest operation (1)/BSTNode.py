class BSTNode:
    # Initializes the BSTNode with the given key. Left, right, and parent
    # are assigned with None.
    def __init__(self, node_key):
        self.key = node_key
        self.left = None
        self.right = None
        self.parent = None

    def get_key(self):
        return self.key

    def get_parent(self):
        return self.parent

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    # get_subtree_key_count() must be overridden in an inheriting class.
    def get_subtree_key_count(self):
        return -1

    # Replace a current child with a new child. Determines if the current child
    # is on the left or right, and calls either set_left() or self.set_right()
    # with the new node, as appropriate.
    # Returns True if the new child is not None, False otherwise.
    def replace_child(self, current_child, new_child):
        if self.left == current_child:
            self.set_left(new_child)
            return True
        elif self.right == current_child:
            self.set_right(new_child)
            return True

        # If neither of the above cases applied, then the new child
        # could not be attached to this node.
        return False

    def set_key(self, new_key):
        self.key = new_key

    def set_left(self, new_left_child):
        # Assign the left child.
        self.left = new_left_child

        # If left child is not None, assign left child's parent.
        if self.left:
            self.left.parent = self

    def set_parent_to_null(self):
        self.parent = None

    def set_right(self, new_right_child):
        # Assign the right child.
        self.right = new_right_child

        # If right child is not None, assign right child's parent.
        if self.right:
            self.right.parent = self
