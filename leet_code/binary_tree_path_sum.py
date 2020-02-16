# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        """
        top-down dfs (node passed to children)
        base case: if leaf, calculate its sum
        """
        sumFound = False 
        
        def helper(root, runningSum, target):
            if not root.left and not root.right:
                if runningSum + root.val == target:
                    sumFound = True
                    print(sumFound, runningSum, root.val)
                    return sumFound
                else:
                    return
            if root.left:
                helper(root.left, root.left.val + runningSum, target)
            if root.right:
                helper(root.right, root.right.val + runningSum, target)
                
            
        sumFound = helper(root, 0, target)
        return sumFound
        