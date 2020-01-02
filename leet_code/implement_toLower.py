class Solution:
    def toLowerCase(self, str: str) -> str:
        """
        Create new blank string
        Loop str:
            if letter is greater than lowercase:
            subtract letter to get lowercase equiv and add to string
            else: add current letter to string
            
        return new string
        """

        new_string = ""

        for letter in str:
            print(ord(letter))
            print('A', ord('A'), 'h', ord('h'))
            if ord(letter) >= ord('A') and ord(letter) <= ord('Z'):
                new_string += chr(ord(letter)+32)
            else:
                new_string += letter
        return new_string


# Runtime: 28 ms, faster than 75.61% of Python3 online submissions for To Lower Case.
# Memory Usage: 12.6 MB, less than 100.00 % of Python3 online submissions for To Lower Case.
