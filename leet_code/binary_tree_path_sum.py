# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
        top-down dfs (node passed to children)
        base case: if leaf, calculate its sum
        """
        sumFound = [False]

        def helper(root, runningSum, sum):
            if not root.left and not root.right:
                if runningSum == sum:
                    sumFound = [True]
                    print(sumFound, 'runningSum:', runningSum,
                          'current value', root.val, sum)
                    return sumFound

            if root.left:
                helper(root.left, root.left.val + runningSum, sum)
                #print(runningSum, root.val)
            if root.right:
                helper(root.right, root.right.val + runningSum, sum)
                #print(runningSum, root.val)

        helper(root, 0, sum)
        print(sumFound)
        return sumFound
