# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root: 
            return 0
        
        def dfs(root, count):
            # base case: if leaf, it is unival
            if not root.left and not root.right:
                return True
            
            # recursive: traverse to child(ren) and determin if each is unival, return True or False
            # compare each child to root to determine if unival
            
            # if subtree, unival, increment count
            return count
        
        
        return dfs(root, 0)
        