class Solution(object): 
    def summaryRanges(self, nums): 
        """ 
        :type nums: List[int] 
        :rtype: List[str] 
        """ 
        output = [] 
        i = 0 
        while i < len(nums): 
            temp = nums[i] 
            while i+1 < len(nums) and nums[i] + 1 == nums[i+1]: 
                i += 1 
            if temp == nums[i]: 
                output.append( str(temp) ) 
            else: 
                output.append( str(temp) + "->" + str(nums[i])) 
            i += 1 
        return output
