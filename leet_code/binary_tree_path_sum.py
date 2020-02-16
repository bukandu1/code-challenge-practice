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
        
        
        Runtime: 48 ms, faster than 22.70% of Python3 online            submissions for Path Sum.
        Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for Path Sum.
        """
        sumFound = [False]

        if not root:
            return False

        def helper(root, runningSum, sum):
            if not root.left and not root.right:
                if runningSum == sum:
                    sumFound[0] = [True]
                    print(sumFound, 'runningSum:', runningSum,
                          'current value', root.val, sum)
                    return

            if root.left:
                helper(root.left, root.left.val + runningSum, sum)
                #print(runningSum, root.val)
            if root.right:
                helper(root.right, root.right.val + runningSum, sum)
                print(runningSum, root.val)

        helper(root, root.val, sum)
        print(sumFound[0], 1)
        return sumFound[0]
