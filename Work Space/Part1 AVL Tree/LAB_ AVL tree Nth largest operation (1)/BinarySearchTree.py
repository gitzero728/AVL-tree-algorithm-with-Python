from abc import ABC, abstractmethod
from BSTNode import BSTNode

class BinarySearchTree:
    def __init__(self):
        self.root = None

    @abstractmethod
    def get_nth_key(self, n):
        pass

    def get_root(self):
        return self.root

    # Performs an inorder traversal of the BST. The visitor's visit() method
    # is called for each node in the tree. visit() returns True to
    # continue traversal, False to stop traversal. If every visit() call
    # returns True, then True is returned. If visit() returns False for any
    # node in the tree then False is returned thus terminating traversal,.
    def in_order(self, visitor, current=None):
        return self.in_order_node(visitor, self.root)

    def in_order_node(self, visitor, current):
        if current:
            # Visit left subtree first, if left child is not None.
            left = current.get_left()
            if left:
                if not self.in_order_node(visitor, left):
                    return False
            # Visit the current node. Return False if the visitor method.
            # returns False.
            if not visitor.visit(current):
                return False

            # Visit right subtree last, if right child is not None.
            right = current.get_right()
            if right:
                return self.in_order_node(visitor, right)

        return True

    def insert_key(self, key):
        self.insert_node(self.make_new_node(key))

    # Attempts to remove a node with a matching key. If no node has a matching
    # key then nothing is done and False is returned. Otherwise the node is
    # removed and True is returned.
    def remove_key(self, key):
        node = self.search(key)
        if not node:
            return False
        else:
            return self.remove_node(node)

    # Searches for a node with a matching key. Returns the node with the
    # matching key, or None if no matching key exists in the tree.
    def search(self, desired_key):
        current_node = self.root
        while current_node:
            # Return the node if the key matches
            if current_node.get_key() == desired_key:
                return current_node
            # Navigate to the left if the search key is
            # less than the node's key.
            elif desired_key < current_node.get_key():
                current_node = current_node.get_left()

                # Navigate to the right if the search key is
                # greater than the node's key.
            else:
                current_node = current_node.get_right()

        # The key was not found in the tree.
        return None

    # Inserts the node into the tree using the standard BST insertion algorithm
    def insert_node(self, node):
        # Check if tree is empty
        if not self.root:
            self.root = node
        else:
            current_node = self.root
            while current_node:
                # Choose to go left or right.
                if node.get_key() < current_node.get_key():
                    # Go left. If left child is not None, insert the new node here.
                    if current_node.get_left() == None:
                        current_node.set_left(node)
                        current_node = None
                    else:
                        # Go left and do the loop again.
                        current_node = current_node.get_left()
                else:
                    # Go right. If the right child is not None, insert the node here.
                    if current_node.get_right() == None:
                        current_node.set_right(node)
                        current_node = None
                    else:
                        # Go right and do the loop again.
                        current_node = current_node.get_right()

    def make_new_node(self, key):
        return BSTNode(key)

    # Removes the node from the tree using the standard BST removal algorithm.
    def remove_node(self, node_to_remove):
        if not node_to_remove:
                return False

        parent = node_to_remove.get_parent()

        # Case 1: Internal node with 2 children.
        if node_to_remove.get_left() and node_to_remove.get_right():
            # Find successor.
            successor_node = node_to_remove.get_right()
            while successor_node.get_left():
                successor_node = successor_node.get_left()

            # Copy the key from the node.
            node_to_remove.set_key(successor_node.get_key())

            # Recursively remove successor and return True.
            self.remove_node(successor_node)
            return True

        # Case 2: self.root node (with 1 or 0 children).
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

        # Case 4: Internal with right child only OR leaf.
        else:
            parent.replace_child(node_to_remove, node_to_remove.get_right())

        return True

    # Performs a left rotation at the given node. Returns the
    # subtree's nroot.
    def rotate_left(self, node):
        parent = node.get_parent()
        right_child = node.get_right()
        right_left_child = right_child.get_left()

        # Replace necessary children from the bottom up.
        node.set_right(right_left_child)
        right_child.set_left(node)
        if parent:
            parent.replace_child(node, right_child)
        else:
            self.root = right_child
            self.root.set_parent_to_null()

        return node.get_parent()

    # Performs a right rotation at the given node. Returns the
    # subtree's new root.
    def rotate_right(self, node):
        parent = node.get_parent()
        left_child = node.get_left()
        left_right_child = left_child.get_right()

        # Replace necessary children from the bottom up.
        node.set_left(left_right_child)
        left_child.set_right(node)
        if parent:
            parent.replace_child(node, left_child)
        else:
            self.root = left_child
            self.root.set_parent_to_null()

        return node.get_parent()
