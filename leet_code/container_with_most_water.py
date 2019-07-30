class Solution:
    def maxArea(self, height: List[int]) -> int:
        #set left = 0
        #set right = last index
        #max_area = 0
        
        left = 0
        right = len(height) - 1
        max_area = 0
        
        #while left and right do not cross
        while left < right:
            #calculate area
            a_height = min(height[left], height[right])
            a_length = right - left
            print(a_height, a_length)
            current_area = a_height * a_length
            print("current area", current_area)
            max_area = max(current_area, max_area)
            print(max_area)
            
            #decide which pointer to move
            #minimum item limits the area so increment the min
            
            if height[left] < height[right]:
                left += 1
                print("inc left")
                
            else:
                right -= 1
                print("dec right")
        
        return max_area
        