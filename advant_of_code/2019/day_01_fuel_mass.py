import unittest

class Solution:
    textfile = "day_01_fuel_mass.txt"

    def fuel_mass(self, textfile):
        file = open(textfile, 'r')
        sum = 0
        for line in file:
            sum += int(line) // 3 - 2

        print(sum)

        return sum


class TestStringMethods(unittest.TestCase):
    def test_mass(self):
        self.assertNotEqual(Solution().fuel_mass("day_01_fuel_mass.txt"), 9827258)
        self.assertEqual(Solution().fuel_mass(
            "day_01_fuel_mass.txt"), 3275518)

    def test_file(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_l(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # s.split should throw when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


unittest.main(exit=False)
