import sys

from BinarySearchTree import BinarySearchTree
from TreeCommands import *
from ExtendedAVLTree import ExtendedAVLTree

def main():
    print("Test 1 - insertion and GetSubtreeKeyCount()")
    test1_passed = test1(sys.stdout)
    print()
    print("Test 2 - insertion, removal, and GetSubtreeKeyCount()")
    test2_passed = test2(sys.stdout)
    print()
    print("Test 3 - insertion, removal, GetSubtreeKeyCount(), and GetNthKey()")
    test3_passed = test3(sys.stdout)

    print("\nSummary:")
    print("Test 1:", 'PASS' if test1_passed else 'FAIL')
    print("Test 2:", 'PASS' if test2_passed else 'FAIL')
    print("Test 3:", 'PASS' if test3_passed else 'FAIL')

def execute_test_cmds(test_commands, test_feedback):
    passed = False
    user_tree = ExtendedAVLTree()
    for cmd in test_commands:
        passed = False
        try:
            passed = cmd.execute(user_tree, test_feedback)
        except:
            print("Runtime error while executing test case")
            return False

        # Break the loop if the command didn't return True.
        if not passed:
            break

    return passed

# Test 1 - insertion and GetSubtreeKeyCount()
# - Insertion of the 7 keys shown in the lab's sample tree
# - Verify keys
# - Verify subtree key counts
def test1(test_feedback):
    test_commands = [
        TreeInsertCommand([10, 20, 30, 55, 42, 19, 77 ]),
        TreeVerifyKeysCommand([10, 19, 20, 30, 42, 55, 77 ]),
        TreeVerifySubtreeCountsCommand([
            (10, 2),
            (19, 1),
            (20, 7),
            (30, 1),
            (42, 4),
            (55, 2),
            (77, 1)
            ])
        ]
    return execute_test_cmds(test_commands, test_feedback)

# Test 2 - insertion, removal, and GetSubtreeKeyCount()
# - Insert 11 keys
# - Verify keys
# - Verify subtree key counts
# - Remove 1 key
# - Verify subtree key counts
def test2(test_feedback):
    test_commands = [
        TreeInsertCommand([86, 75, 23, 30, 98, 67, 53, 9, 19, 58, 14]), # 11 keys
        TreeVerifyKeysCommand([9, 14, 19, 23, 30, 53, 58, 67, 75, 86, 98]),
        TreeVerifySubtreeCountsCommand([
            (9, 2),
            (14, 1),
            (19, 4),
            (23, 1),
            (30, 11),
            (53, 1),
            (58, 3),
            (67, 1),
            (75, 6),
            (86, 2),
            (98, 1)
        ]),
        TreeRemoveCommand([75]),
        TreeVerifySubtreeCountsCommand([
            (9, 2),
            (14, 1),
            (19, 4),
            (23, 1),
            (30, 10),
            (53, 1),
            (58, 3),
            (67, 1),
            (86, 5),
            (98, 1)
        ])
    ]
    return execute_test_cmds(test_commands, test_feedback)

# Test 3 - insertion, removal, GetSubtreeKeyCount(), and GetNthKey()
# - Insert 18 keys
# - Verify keys
# - Test GetNthKey()
# - Verify subtree key counts
def test3(test_feedback):
    keys_to_insert = [10, 58, 66, 18, 34, 96, 5, 48, 73, 62, 36, 16, 23, 99, 92, 95, 46, 97]
    sorted_keys = [5, 10, 16, 18, 23, 34, 36, 46, 48, 58, 62, 66, 73, 92, 95, 96, 97, 99]

    test_commands = [
        TreeInsertCommand(keys_to_insert),
        TreeVerifyKeysCommand(sorted_keys),
        TreeGetNthCommand(11, 66),
        TreeGetNthCommand(7, 46),
        TreeGetNthCommand(15, 96),
        TreeGetNthCommand(4, 23),
        TreeVerifySubtreeCountsCommand([
                (5, 1),
                (10, 3),
                (16, 1),
                (18, 9),
                (23, 1),
                (34, 2),
                (36, 5),
                (46, 1),
                (48, 2),
                (58, 18),
                (62, 1),
                (66, 2),
                (73, 8),
                (92, 2),
                (95, 1),
                (96, 5),
                (97, 1),
                (99, 2)
        ]),
        TreeRemoveCommand([58]),
        TreeVerifySubtreeCountsCommand([
                (5, 1),
                (10, 3),
                (16, 1),
                (18, 9),
                (23, 1),
                (34, 2),
                (36, 5),
                (46, 1),
                (48, 2),
                (62, 17),
                (66, 1),
                (73, 4),
                (92, 2),
                (95, 1),
                (96, 7),
                (97, 1),
                (99, 2)
            ]),
        TreeGetNthCommand(9, 62),
        TreeGetNthCommand(3, 18),
        TreeGetNthCommand(10, 66),
        TreeGetNthCommand(5, 34)
        ]

    return execute_test_cmds(test_commands, test_feedback)

if __name__ == '__main__':
    main()
