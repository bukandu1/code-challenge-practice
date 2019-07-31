class Solution:
    def validPalindrome(self, s: str) -> bool:
        #abca --> acba
        #abcca --> ab
        
        if len(str) == 1:
            return True
        
        if not str:
            return False
        
        i = 0
        j = len(str) - 1
        extra_letter = 0
        
        while pointers have not crossed:
            compare the letters at the current pointers
            if str[i] == str [j]:
                increase i
                decrease j
            else:
                if str[i] == str[j-1]:
                    extra_letter += 1
                    j -= 1
                elif str[i+1]
        