class Solution:
    def happy_number(self, num):
        seen_set = set()
        happy_num = num
        
        while happy_num != 1:
            seen_set.add(happy_num)
            divisor = 10
            sum = 0

            while divisor < happy_num:
                sum += pow(happy_num % divisor)
                happy_num = happy_num // divisor

            sum += pow(happy_num % divisor)

            happy_num = happy_num % divisor

            if happy_num in seen_set:
                return False

        return True

