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

        def helper(A, start, end):
            if start > end:
                return None
            if start == end:
                return TreeNode(A[start])

            else:
                mid = int((start + end)/2)
                print('mid:', mid)
                rootnode = TreeNode(A[mid])

                rootnode.left = helper(A, start, mid-1)
                rootnode.right = helper(A, mid+1, end)

                return rootnode

        return helper(nums, 0, len(nums) - 1)


# LC: 108 Runtime: 72 ms, faster than 65.94 % of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
# Memory Usage: 14.8 MB, less than 100.00 % of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
