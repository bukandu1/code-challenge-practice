class Solution:

    # naive solution
    def longestPalindrome(self, s: str) -> str:
        #start with first two letters
        if not s:
            return ""

        if len(s) < 1:
            return s

        current_max = s[0]

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                #If a palindome found, compare to current max
                substring = s[i:j+1]
                #print(f'substring: {substring} and backward: {substring[::-1]}')
                if substring == substring[::-1]:
                    if len(substring) > len(current_max):
                        current_max = s[i:j+1]

        return current_max

    # more optimal solutiongit
    def longestPalindromeopt(self, s: str) -> str:
        return
