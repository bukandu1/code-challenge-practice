# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        1.determine root (create node)
        2.recursively construct left subtree
        3.recursively construct right subtree
        
        local problem: create elements/nodes in subarray
        
        if sorted, root is middle value (create Node)
        answers may not be unique
        
        time complexity: O(n) * (calculation for each)
        space: call stack space will only grow at most O(logn) (equivalent to the height of the tree)
        
        """

        return helper(nums, 0, len(nums) - 1)
