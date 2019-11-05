class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sum_dict = {}
        
        for i in range(len(nums)):
            if target - nums[i] in sum_dict:
                return [i, sum_dict[target - nums[i]]]
            sum_dict[nums[i]] = i
        

# Runtime: 60 ms, faster than 70.98% of Python3 online submissions for Two Sum.
# Memory Usage: 14.9 MB, less than 11.39 % of Python3 online submissions for Two Sum.
