# Runtime: 20 ms, faster than 98.59% of Python3 online submissions for Remove Vowels from a String.#
# Memory Usage: 12.6 MB, less than 100.00 % of Python3 online submissions for Remove Vowels from a String.


class Solution:
    def removeVowels(self, S: str) -> str:
        """
        set = (a, e, i , o, u)
        
        create list from string
        loop string
            if current letter is in string, then update the 
            
        return joined string
        """

        vowel_set = ('a', 'e', 'i', 'o', 'u')

        string_list = list(S)

        for i in range(len(string_list)):
            if string_list[i] in vowel_set:
                string_list[i] = ''

        print(string_list)

        return ''.join(string_list)
