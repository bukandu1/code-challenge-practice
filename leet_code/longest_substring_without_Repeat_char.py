# 7/23/19
# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


# Naive  Solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #traversing string  
            #keep track of each letter
            #when a repeating letter found compare if the len(substring) is > max
            #return max
        
        substring = ""
        seen_set = set()
        max_length = 0
        
        if len(s) < 2 :
            return len(s)
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                #print(f'index {j} looking at {s[j]} now and length of s is {len(s)}')
                
                if s[j] not in seen_set:
                    #print(f'putting {s[j]} in seen_set')
                    substring += s[j]
                    
                    seen_set.add(s[j])
                   
                else:
                    #print(substring)
                    #print("Seen Set:", seen_set, "\n")
                    max_length = max(len(substring), max_length)
                    substring = ""
                    seen_set = set()
                    break
            
            max_length = max(len(substring), max_length)
            
        #print(max_length)
        
        return max_length
                
            
                
            
            
        