from abc import ABC, abstractmethod
from BinarySearchTree import BinarySearchTree
from BSTNodeListVisitor import BSTNodeListVisitor

current_tree = None

class TreeTestCommand:
    @abstractmethod
    def execute(self):
        pass

class TreeInsertCommand(TreeTestCommand):
    def __init__(self, keys):
        self.keys_to_insert = keys

    def execute(self, tree, test_feedback):
        # If no keys to insert, return True immediately.
        if 0 == len(self.keys_to_insert):
            return True

        # Begin feedback message.
        print("Inserting keys:", self.keys_to_insert, file=test_feedback)

        for key in self.keys_to_insert:
            tree.insert_key(key)

        return True

class TreeRemoveCommand(TreeTestCommand):
    def __init__(self, keys):
        self.keys_to_remove = keys

    def execute(self, tree, test_feedback):
        if len(self.keys_to_remove) > 0:
            # Begin feedback message and remove first key.
            print("Removing keys:", self.keys_to_remove, file=test_feedback)

            # Remove keys.
            for key in self.keys_to_remove:
                tree.remove_key(key)
        return True

class TreeVerifyKeysCommand(TreeTestCommand):
    def __init__(self, keys):
        self.expected_keys = keys

    def execute(self, tree, test_feedback):
        # Create a BSTNodeStringVisitor and do an in order traversal.
        visitor = BSTNodeListVisitor();
        tree.in_order(visitor)

        # The visitor determines if a circular reference exists.
        if visitor.has_circular_reference():
            print(f"""FAIL: Tree traversal encountered the same node more than once, \
so a circulare reference exists""")
            return False

        # Make a list of keys from the visitor's string of nodes.
        actual = []
        for node in visitor.visited_nodes:
            actual.append(node.get_key())

        # Compare actual to expected.
        passed = True

        if len(actual) == len(self.expected_keys):
            for actual_key, expected_key in zip(actual, self.expected_keys):
                if actual_key != expected_key:
                    passed = False
        else:
            passed = False

        # Display passed.
        print(f"""{"PASS" if passed else "FAIL"}: Inorder key verification
  Expected: {self.expected_keys}
  Actual:   {actual}""",
              file=test_feedback)

        return passed

    def print_string(self, lst, test_feedback):
        if len(lst) > 0:
            # Output the list.
            print(lst, file=test_feedback,)

class TreeGetNthCommand(TreeTestCommand):
    def __init__(self, n, expected_key):
        self.n = n
        self.expected_key = expected_key

    def execute(self, tree, test_feedback):
        actual_key = tree.get_nth_key(self.n)
        if actual_key == self.expected_key:
            print(f"""PASS: get_nth_key({self.n}) returned {actual_key}""",
                  file=test_feedback)
            return True

        # Actual key does not equal expected.
        print(f"""FAIL: get_nth_key({self.n}) returned {actual_key}, but expected key is {self.expected_key}""",
              file=test_feedback)
        return False

class TreeVerifySubtreeCountsCommand(TreeTestCommand):
    def __init__(self, expected_key_count_pairs):
        self.expected_pairs = expected_key_count_pairs

    def execute(self, tree, test_feedback):
        # Create a BSTNodeStringVisitor and do an in order traversal.
        visitor = BSTNodeListVisitor()
        tree.in_order(visitor)

        # Compare actual to expected.
        passed = True
        if len(visitor.visited_nodes) == len(self.expected_pairs):
            for actual_node, expected_pair in zip(visitor.visited_nodes, self.expected_pairs):
                # Get the actual node's subtree key count.
                actual_count = actual_node.get_subtree_key_count()

                # Compare actual vs. expected subtree key count.
                if actual_count != expected_pair[1]: 
                    print(f"""FAIL: Node with key {actual_node.get_key()} has a \
subtree count of {actual_count}, \
but the expected subtree key count is {expected_pair[1]}""",
                          file=test_feedback)
                    passed = False
                else:
                    print(f"""PASS: Node with key {actual_node.get_key()} has a subtree key \
count of {actual_count}""",
                          file=test_feedback)

            if not passed:
                return  False

            # Display results.
            print(f"""PASS: All {len(self.expected_pairs)} nodes have correct subtree key counts""",
                  file=test_feedback)
            return True

        # Give feedback indicating that the number of nodes in the tree is incorrect.
        phrase = ("only one node was"
                  if len(self.expected_pairs) == 1
                  else f"""{len(self.expected_pairs)} nodes were""")
        print(f"""FAIL: Traversal through tree encountered {len(visitor.visited_nodes)} \
nodes before either stopping or encountering a circular reference. \
However, {phrase} expected in the tree.""",
              file=test_feedback)
        return False
