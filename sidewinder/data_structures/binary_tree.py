#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

# Source: https://youtu.be/6oL-0TdVy28


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")

    def preorder_print(self, start, traversal):
        """ Preorder traversal. Root -> Left -> Right """
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """ In-order traversal. Left -> Root - Right """
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """ Post-order traversal. Left -> Right -> Root """
        if start:
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
            traversal += (str(start.value) + '-')
        return traversal

# Tree representation.
#          1
#        /   \
#       2     3
#      / \   / \
#     4   5 6   7
# Pre-order:    1-2-4-5-3-6-7-
# In-order:     4-2-5-1-6-3-7-
# Post-order:   2-4-5-3-6-7-1-
# It's all DFS Depth First Search


# Binary tree setup.
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree('preorder'))
print(tree.print_tree('inorder'))
print(tree.print_tree('postorder'))
