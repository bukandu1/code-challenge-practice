class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewel_list = set(J)
        count = 0
        for stone in S:
            if stone in jewel_list:
                count += 1
        return count
    
# Runtime: 24 ms, faster than 98.91% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Jewels and Stones.