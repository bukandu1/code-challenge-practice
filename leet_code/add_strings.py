"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        def convertToNum(num):
            numDict = {"1": 1, "2": 2, "3": 3, "4": 4, '5': 5, '6': 6, '7':             7, '8': 8, '9': 9, '0': 0}
            new_num =  0
            multiplier = 1
            for digit in num[::-1]:
                new_num += numDict[digit] * multiplier
                multiplier *= 10
            print(new_num)
            return new_num
        
        return str(convertToNum(num1) + convertToNum(num2))
        
        
