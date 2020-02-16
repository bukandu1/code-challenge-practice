# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Runtime: 40 ms, faster than 18.97% of Python3 online submissions for Count Univalue Subtrees.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Count Univalue Subtrees.
"""
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.count = 0

        def dfs(root):
            # base case: if leaf, it is unival
            if not root.left and not root.right:
                self.count += 1
                return True

            isUnival = True
            # recursive: traverse to child(ren) and determin if each is unival, return True or False
            # compare each child to root to determine if unival
            if root.left:
                leftST = dfs(root.left)
                if not leftST or root.left.val != root.val:
                    isUnival = False
                print('root.left.val', root.left.val, 'root val',
                      root.val, isUnival, 'count', self.count)

            if root.right:
                rightST = dfs(root.right)
                if not rightST or root.right.val != root.val:
                    isUnival = False
                print('root.right.val', root.right.val, 'root val',
                      root.val, isUnival, 'count', self.count)

            # if subtree, unival, increment count
            if isUnival:
                self.count += 1

            return isUnival

        dfs(root)
        return self.count
