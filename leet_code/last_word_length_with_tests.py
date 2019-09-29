import unittest

class Solution:
""" 
Runtime: 32 ms, faster than 90.06% of Python3 online submissions for Length of Last Word.
Memory Usage: 13.9 MB, less than 5.26% of Python3 online submissions for Length of Last Word.

"""
    def lengthOfLastWord(self, s: str) -> int:
        #return 0 if null
        if not s:
            return 0

        #split string on the spaces
        s_list = s.split(' ')

        if len(''.join(s_list)) == 0:
            return 0

        if s_list[-1] == '':
            i = -1
            while (s_list[i] == ''):
                i -= 1

            print(s_list)
            return len(s_list[i])

        #look at last item in list
        return len(s_list[-1])

class TestLastWordLength(unittest.TestCase):

    #TODO: Add setup and tear down for Solution class
    def test_null(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLastWord(''), 0)

    def test_withOneWord(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLastWord('Hello'), 5)

    def test_withTwoWords(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLastWord('Hello Worlds.'), 7)

    def test_withEndWithSpace(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLastWord("a    "), 1)
       
    def test_withOnlySpaces(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLastWord("   "), 0)

