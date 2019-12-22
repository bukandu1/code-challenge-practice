import unittest

class Solution:
    def happy_number(self, num):
        print('happy number is: ', num)
        seen_set = set()
        happy_num = num
        
        while happy_num != 1:
            seen_set.add(happy_num)
            divisor = 10
            sum = 0

            while divisor <= happy_num:
                digit = happy_num % divisor
                sum += pow(digit, 2)
                happy_num = happy_num // divisor
                print('digit: ', digit, 'happy_num: ', happy_num)
                

            sum += pow(happy_num, 2)
            print('final sum is: ', sum)
            # print('digit: ', digit, 'happy_num: ', happy_num)
            #print(sum)

            happy_num = sum

            print(seen_set)
            if happy_num == 1:
                return True 

            elif happy_num in seen_set:
                return False


class TestHappyNumber(unittest.TestCase):
    def setUp(self):
        self.file = "day_01_fuel_mass.txt"
        self.s = Solution()

    def test_happyNumberTrue(self):
        # setup
        happy_number = 82
        result = self.s.happy_number(happy_number)

        self.assertTrue(result)

    def test_happyNumberFalse(self):
        happy_number = 22
        result = self.s.happy_number(happy_number)

        self.assertFalse(result)
    
    def test_happyNumberTrueOneDigit(self):
        happy_number = 1
        result = self.s.happy_number(happy_number)
        self.assertFalse(result)

    def test_happyNumberFalseOneDigit(self):
        happy_number = 2
        result = self.s.happy_number(happy_number)

        self.assertFalse(result)


unittest.main(exit=False)
