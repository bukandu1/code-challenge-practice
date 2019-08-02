class Solution:
    def validPalindrome(self, s: str) -> bool:
        #abca --> acba
        #abcca --> ab
        if not s:
            return False

        backward_string = s[::-1]
        print(backward_string)
        extra_letter = 0
        
        i = 0
        j = len(backward_string) - 1
        while i < len(backward_string):
            #compare the letters at the current pointers
            if s[i] != backward_string[j]:
                extra_letter += 1
                j-=1
            else:
                i+=1
                j-=1
                    
            if extra_letter > 1: 
                    return False

        return True
        