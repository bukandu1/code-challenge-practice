class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            num = -1 * int(str(x)[:0:-1])
        else:
            num = int(str(x)[::-1])

        return 0 if num <= -2 ** 31 or num > 2 ** 31 else num


# Runtime: 52 ms, faster than 7.21% of Python3 online submissions for Reverse Integer.
# Memory Usage: 13.9 MB, less than 5.26% of Python3 online submissions for Reverse Integer
