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
            h1 = helperBalancedHeight(node.left)
            h2 = helperBalancedHeight(node.right)

            if h1 == -1 or h2 == -1:
                return -1

            if (abs(h1 - h2) > 1):
                return -1

            if h1 > h2:
                return h1 + 1

            return h2 + 1

        if helperBalancedHeight(node) > -1:
            return True
        else:
            return False

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)

n1.left = n2
n1.right = n3

n2.left = n4
n3.left = n6
n3.right = n7
n7.left = n8
n8.left = n9

sol = Solution()
print(sol.isBalanced(n1))
