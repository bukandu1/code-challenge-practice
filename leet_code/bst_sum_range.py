# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        def helper(root, L, R, sum_array):

            if root.left:
                helper(root.left, L, R, sum_array)
            if L <= root.val and root.val <= R:
                sum_array.append(root.val)
            if root.right:
                helper(root.right, L, R, sum_array)

            return sum_array

        sum_array = []
        return sum(helper(root, L, R, sum_array))


# Runtime: 268 ms, faster than 42.52 % of Python3 online submissions for Range Sum of BST.
# Memory Usage: 20.7 MB, less than 100.00 % of Python3 online submissions for Range Sum of BST.
