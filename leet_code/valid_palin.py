class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = list(s)
        print(lst)
        
        i=0
        j=len(lst)-1
        
        while(i<j):
            if not lst[i].isalnum():
                i+=1
            elif not lst[j].isalnum():
                j-=1
            else:
                if lst[i].lower() == lst[j].lower():
                    i+=1
                    j-=1
                else:
                    return False
        
        return True
            
        