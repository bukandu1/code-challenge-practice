# Given a binary tree, write a function to determine whether the tree is balanced

class Node():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class Solution:
    def isBalanced(self, node):

        def helperBalancedHeight(node):
            if not node:
                return 0
            h1 = helperBalancedHeight(n.left)
            h2 = helperBalancedHeight(n.right)

            if h1 == -1 or h2 == -1:
                return -1
