import unittest

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #return 0 if space or null
        if not s:
            return 0
        
        if len(s.split()) == 0:
            return 0

        if s[-1] == " ":
            return 1

        #split string on the spaces & look at last item in list.
        return len(s.split(' ')[-1])

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
        self.assertEqual(sol.lengthOfLastWord("a "), 1)
       
    def test_withEndWithSpace(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLastWord("   "), 0)

