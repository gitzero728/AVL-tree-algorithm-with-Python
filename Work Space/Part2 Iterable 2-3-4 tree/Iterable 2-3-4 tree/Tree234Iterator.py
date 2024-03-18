class Tree234Iterator:
    def __init__(self, root):
        # Initialize a stack to store nodes and their key indices
        self.stack = []
        # Start from the root and traverse to the leftmost node,
        # pushing all the nodes and their key indices to the stack
        self._traverse_left(root)

    def _traverse_left(self, node):
        # This method takes a node and traverses to its leftmost child,
        # pushing all the nodes and their key indices to the stack
        while node is not None:
            # For each node, push all its keys to the stack in reverse order
            for i in reversed(range(node.get_key_count())):
                self.stack.append((node, i))
            
            # Move to the left child of the current node
            node = node.get_child(0)

    def __next__(self):
        # This method is called when the next element is requested in iteration
        if not self.stack:
            # If the stack is empty, it means we have iterated through all the keys,
            # so we raise the StopIteration exception to end the iteration
            raise StopIteration

        # Pop the node and key index from the stack
        node, key_index = self.stack.pop()

        # If the node has a right child (child at the index of the key + 1),
        # push all the leftmost nodes of the right child to the stack
        if node.get_child(key_index + 1) is not None:
            self._traverse_left(node.get_child(key_index + 1))

        # Return the key at the popped key index in the node
        return node.get_key(key_index)
