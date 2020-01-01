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


class TestZeroMatric(unittest.TestCase):
    def TestNEqualOneNoAZeros(self, mat):
        pass

    def TestNEqualOneWithZero(self, mat):
        pass

    def TestNEqualTwoWithZero(self, mat):
        pass

    def TestNEqualThreeWithZero(self, mat):
        pass

