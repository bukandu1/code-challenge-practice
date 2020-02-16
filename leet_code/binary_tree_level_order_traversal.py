# 102. Binary Tree Level Order Traversal

# Runtime: 28 ms, faster than 91.77 % of Python3 online submissions 
# for Binary Tree Level Order Traversal.
# Memory Usage: 13 MB, less than 100.00 % of Python3 online 
# submissions for Binary Tree Level Order Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # create queue
        # push root to queue
        # while queue not empty:
            # pop FI node
            # if node has R or L node, push to queue

        queue = deque([]) #append and popleft
        level = 0
        result = []
        
        if not root:
            return []
        
        queue.append((root, level))

        while queue:
            current, currLevel = queue.popleft()
            if currLevel >= len(result):
                     result.append([])

            result[currLevel].append(current.val)

            if current.left:
                queue.append((current.left, currLevel + 1))

            if current.right:
                queue.append((current.right, currLevel + 1))

        return result

            
        
        
