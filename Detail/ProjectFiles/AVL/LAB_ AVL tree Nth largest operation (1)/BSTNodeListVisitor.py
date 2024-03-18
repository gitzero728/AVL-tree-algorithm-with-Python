from BSTNodeVisitor import BSTNodeVisitor

class BSTNodeListVisitor(BSTNodeVisitor):
    # visited_set is used to ensure that the exact same node instance is not
    # visited more than once.
    def __init__(self):
        super().__init__()
        self.visited_set = set()
        self.visited_nodes = list()
        self.has_circ_ref = False

    # Returns True if a circular reference was discovered when
    # visiting a node, False otherwise.
    def has_circular_reference(self, ):
        return self.has_circ_ref

    def visit(self, node):
        # Check if the node was already visited. If so, the tree has a
        # circular reference.
        if node in self.visited_set:
            # visited_set has_circular reference.
            self.has_circ_ref = True

            # Return False to stop infinite traversal.
            return False

        # Add node to set and string.
        self.visited_set.add(node)
        self.visited_nodes.append(node)

        # Return True to continue traversal.
        return True
