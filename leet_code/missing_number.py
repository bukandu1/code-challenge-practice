class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_list = sum(nums)
        
        actual_sum = 0
        for i in range(0, len(nums) + 1):
            actual_sum += i
            
        return actual_sum - sum_list
        
"""
Runtime: 128 ms, faster than 97.99% of Python3 online submissions for Missing Number.
Memory Usage: 13.9 MB, less than 95.16% of Python3 online submissions for Missing Number.

"""
