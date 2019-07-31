class Solution:
    def validPalindrome(self, s: str) -> bool:
        #abca --> acba
        #abcca --> ab
        if not s:
            return False
        
        if len(s) == 1:
            return True

        i = 0
        j = len(s) - 1
        extra_letter = 0
        
        while i < j:
            print(i, j, extra_letter)
            #compare the letters at the current pointers
            if s[i] == s[j]:
                i +=1 
                j -= 1
            else:
                if s[i] == s[j-1]:
                    extra_letter += 1
                    j -= 1
                elif s[i+1] == s[j]:
                    extra_letter += 1
                    i += 1
                else:
                    return False
            if extra_letter > 1:
                return False
        
        return True
        