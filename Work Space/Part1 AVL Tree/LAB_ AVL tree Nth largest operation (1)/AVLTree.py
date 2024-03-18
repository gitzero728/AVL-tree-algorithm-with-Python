from BinarySearchTree import BinarySearchTree
from AVLNode import AVLNode

class AVLTree(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def insert_node(self, node):
        # AVL insertion starts with the standard BST insertion.
        super().insert_node(node)

        # Then rebalancing occurs along a path from the new node's
        # parent up to the root.
        node = node.get_parent()
        while node:
            self.rebalance(node)
            node = node.get_parent()

    # Updates the given node's height and rebalances the subtree if the
    # balance factor is now -2 or +2. Rebalancing is done by performing one
    # or two rotations. Returns the subtree's new root if a rotation
    # occurred, or the node itself if no rebalancing was required.
    def rebalance(self, node):
        # First update the height of this node.
        node.update_height()

        # Check for an imbalance.
        if node.get_balance() == -2:
            # The subtree is too big to the right.
            right_child = node.get_right()
            if right_child.get_balance() == 1:
                # Double rotation case. First do a right rotation
                # on the right child.
                self.rotate_right(node.get_right())

            # A left rotation will now make the subtree balanced.
            return self.rotate_left(node)

        elif node.get_balance() == 2:
            # The subtree is too big to the left.
            left_child = node.get_left()
            if left_child.get_balance() == -1:
                # Double rotation case. First do a left rotation
                # on the left child.
                self.rotate_left(node.get_left())

            # A right rotation will now make the subtree balanced.
            return self.rotate_right(node)

        # No imbalance, so just return the original node.
        return node

    def remove_AVLNode(self, node_to_remove):
        if not node_to_remove:
            return False

        # Parent needed for rebalancing.
        parent = node_to_remove.get_parent()

        # Case 1: Internal node with 2 children.
        if node_to_remove.get_left() and node_to_remove.get_right():
            # Find successor.
            successor_node = node_to_remove.get_right()
            while successor_node.get_left():
                successor_node = successor_node.get_left()

            # Copy the key from the node.
            node_to_remove.set_key(successor_node.get_key())

            # Recursively remove successor.
            self.remove_node(successor_node)

            # Nothing left to do since the recursive call will have rebalanced.
            return True

        # Case 2: Root node (with 1 or 0 children).
        elif node_to_remove == self.root:
            if node_to_remove.get_left():
                self.root = node_to_remove.get_left()
            else:
                self.root = node_to_remove.get_right()

            if self.root:
                self.root.set_parent_to_null()

                return True

        # Case 3: Internal with left child only.
        elif node_to_remove.get_left():
            parent.replace_child(node_to_remove, node_to_remove.get_left())

            return True

        # Case 4: Internal with right child only OR leaf.
        else:
            parent.replace_child(node_to_remove, node_to_remove.get_right())

        # Anything that was below node_to_remove that has persisted is already
        # correctly balanced, but ancestors of node_to_remove may need rebalancing.
        node_to_rebalance = parent
        while node_to_rebalance:
            self.rebalance(node_to_rebalance)
            node_to_rebalance = node_to_rebalance.get_parent()

        return True

    def remove_node(self, node_to_remove):
        return self.remove_AVLNode(node_to_remove)
