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
            

