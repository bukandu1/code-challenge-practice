import unittest

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()

    def push(self, x: int) -> None:
        #add item to end
        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


class TestLastWordLength(unittest.TestCase):

    #TODO: Add setup and tear down for Solution class
    def test_stackImplementation(self):
        obj = MinStack()
        obj.push(-2)
        obj.push(0)
        obj.push(-3)

        self.assertEqual(obj.getMin(), -3)

        obj.pop()
        param_3 = obj.top()
        param_4 = obj.getMin()
        self.assertEqual(param_3, 0)
        self.assertEqual(param_4, -2)



