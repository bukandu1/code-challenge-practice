import unittest

class Solution:
    def zero_matrix(self, mat):
        """
        loop row:
            loop col
                if row/col == 0:
                    save row and col
                    break
        loop col and row:
            update each index val to 0

        for i in range(0, n):
            mat[row][i] = 0
            mat[i][row] = 0

        """

        return True


class TestZeroMatric(unittest.TestCase):
    def setUp(self):
        self.s = Solution

    def TestNEqualOneNoAZeros(self):
        mat = [1]

    def TestNEqualOneWithZero(self):
        mat = [0]

    def TestNEqualTwoWithZero(self):
        mat = [[1,1,],
               [1,1,]]

        result = self.s.zero_matrix(mat)
        

    def TestNEqualThreeWithZero(self):
        mat = [[1, 1, 1],
               [1, 1, 1],
               [1, 0, 1]]

