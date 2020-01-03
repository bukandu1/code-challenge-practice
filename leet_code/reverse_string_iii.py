class Solution:
    def reverseWords(self, s: str) -> str:
        # "" -> ""
        # "a" -> "a"
        # "at today" -> "ta yadot"
        
        """
        split the string at the spaces
        [Let's, take,  LeetCode, contest]
        loop list and reverse each index
        return joined list
        """
        
        split_list = s.split()
        
        for i in range(len(split_list)):
            split_list[i] = split_list[i][::-1]
        
        return " ".join(split_list)

# Runtime: 24 ms, faster than 96.11% of Python3 online submissions for Reverse Words in a String III.
# Memory Usage: 13.3 MB, less than 96.15% of Python3 online submissions for Reverse Words in a String III.
            

