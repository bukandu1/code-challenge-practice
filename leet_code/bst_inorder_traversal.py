# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(root, lst):
            if root:
                helper(root.left, lst)
                lst.append(root.val)
                helper(root.right, lst)
            return lst

        return helper(root, [])
