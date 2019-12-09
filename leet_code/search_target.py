# Given a sorted array and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.


import unittest
class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            index = (right + left) // 2
            if nums[index] == target:
                return index
            elif nums[index] < target:
                left = index + 1
                print('higher', index)
            else:
                right = index - 1
                print('lower', index)

        print('index final:', index)
        if target < nums[index]:
            return index
        else:
            return index + 1

        
class TestStringMethods(unittest.TestCase):
    def test_isLocated(self):
        s = Solution()
        result = s.searchInsert([1,3,5], 5)
        self.assertEqual(result, 2)

    def test_located2(self):
        s = Solution()
        result = s.searchInsert([1, 3, 5], 6)
        self.assertEqual(result, 3)

    def test_located3(self):
        s = Solution()
        result = s.searchInsert([1, 3, 5, 6], 2)
        self.assertEqual(result, 1)
            

    def test_located4(self):
        s = Solution()
        result = s.searchInsert([1, 3, 5, 6], 0)
        self.assertEqual(result, 0)

unittest.main(exit=False)
