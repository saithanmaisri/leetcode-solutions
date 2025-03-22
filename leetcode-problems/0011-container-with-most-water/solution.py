class Solution(object): 
    def maxArea(self, height): 
        n = len(height) 
        max_water = 0 
        i = 0 
        j = n-1 
        while i < j: 
            cur_height = min(height[i], height[j]) 
            cur_base = j-i 
            cur_water = cur_height * cur_base 
            max_water = max(max_water, cur_water) 
            if height[i] < height[j]: 
                i+=1 
            else: 
                j-=1 
        return max_water
