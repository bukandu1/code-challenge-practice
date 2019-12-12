import unittest

class Solution:
    textfile = "day_01_fuel_mass.txt"

    def fuel_mass(self, textfile):
        file = open(textfile, 'r')
        sum = 0
        for line in file:
            sum += int(line) // 3 - 2

        print(sum)
        file.close()

        return sum

    def deplete_fuel(self, textfile):
        file = open(textfile, "r")
        sum = 0 
        mass = int(file.readline())
        fuel = mass // 3 - 2
        while mass >= fuel:
            
            sum += fuel
            if mass >= fuel:
                mass -= fuel
            else: 
                break
    
            mass = int(file.readline())
            fuel = mass // 3 - 2

        file.close()
        return sum

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.file = "day_01_fuel_mass.txt"

    def test_mass(self):
        self.assertNotEqual(Solution().fuel_mass(self.file), 9827258)
        self.assertEqual(Solution().fuel_mass(
            "day_01_fuel_mass.txt"), 3275518)

    def test_deplete_fuel(self):
        self.assertEqual(Solution().deplete_fuel(self.file), 79)
        self.assertFalse('Foo'.isupper())

    def test_l(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # s.split should throw when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


unittest.main(exit=False)
