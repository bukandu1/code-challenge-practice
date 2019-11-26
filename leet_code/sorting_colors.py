class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if curr == 2, do nothing
        # if curr == 0
            # switch with index at the begin 
            # increase index by 1
        # if curr == 1
            # switch with index at end
            # decrease by 1
        
        i = 0
        curr = 0
        j = len(nums) - 1

        while curr <= j:
            print("before", nums)
            if nums[curr] == 0:
                nums[curr], nums[i] = nums[i], nums[curr]
                i += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[j] = nums[j], nums[curr]
                j -= 1
            else:
                curr += 1
            print('after', nums, 'curr', curr, 'i', i, 'j:', j,)
        
        