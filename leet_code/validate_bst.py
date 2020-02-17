"""     1
     /\     <- False
    2   3

null <- True
1 <- True
        6
        /\\
    3       8       <- False
            /\\
           7   9

inorder tree traversal (L -> root -> R)
- compare the prev_node to the next_node visited
    -if prev_node > next_node
        return False
- one at the end of the tree (nothing else to_visit)
    return True (assume that all nodes prior to ending node is smaller)
    """


class Node():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.isValid = True

        if not root:
            return True

        def isValid(root):
            if not root.left and not root.right:
                return True

            if root.left:
                #traverse right and compare to root
                leftST = isValid(root.left)
                self.isValid = leftST and root.left.val < root.val

            if root.right:
                rightST = isValid(root.right)
                self.isValid = rightST and root.right.val > root.val

        isValid(root)
        return self.isValid


