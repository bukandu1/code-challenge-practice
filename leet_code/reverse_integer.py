class Solution:
    """
    Runtime: 24 ms, faster than 93.56% of Python3 online submissions for Reverse Integer.
    Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Reverse Integer.

    """
    def reverse(self, x: int) -> int:
        #if x <= -2 ** 31 or x >= 2 ** 31 - 1:
        #    return 0
        
        sum = 0
        multiplier = 1
        for digit in str(abs(x)):
            sum += int(digit) * multiplier
            multiplier *= 10

        if sum <= -2 ** 31 or sum >= 2 ** 31:
            return 0
        
        return sum if x >= 0 else sum * -1

    
            
        
        
        
