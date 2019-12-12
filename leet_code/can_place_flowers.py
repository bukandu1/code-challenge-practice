class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter = 0
        i = 0
        lst = flowerbed
        if sum(flowerbed) == 0:
            if len(flowerbed) % 2 == 1:
                return len(flowerbed) // 2 + 1 >= n
            else:
                return len(flowerbed) // 2 >= n

        if (len(lst) % 2 == 0 and sum(lst) == len(lst)//2) or (len(lst) % 2 == 1 and sum(lst) == len(lst)//2 + .5):
            return n == 0

        if len(lst) >= 2:
            if i == 0 and lst[i] == 0 and lst[i+1] == 0:
                counter += 1
                lst[i] = 1
                i += 1
                #print('first index')

        while i < len(flowerbed) - 1:
            if lst[i] == 0 and lst[i-1] == 0 and lst[i+1] == 0:
                counter += 1
                lst[i] = 1
                #print('zeuros everywhere')
            i += 1
            #print(lst, counter)

        if lst[i-1] == 0 and lst[i] == 0:
            counter += 1
            #print('secoud to last is 0')

        #print('n', n, 1, 'counter', counter)
        return n <= counter
