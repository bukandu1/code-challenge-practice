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
            height = min(left, right)
            length = right - left
            current_area = height * length
            max_area = max(current_area, max_area)
            
            #decide which pointer to move
            #minimum item limits the area so increment the min
        