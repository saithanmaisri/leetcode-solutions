class Solution(object): 
    def containsNearbyDuplicate(self, nums, k): 
        """ 
        :type nums: List[int] 
        :type k: int 
        :rtype: bool 
        """ 
        # Dictionary to store the last index of each element 
        hsh = {} 
        # Iterate through the list 
        for i in range(len(nums)): 
            # If the element is already in the dictionary and the current index - last index <= k 
            if nums[i] in hsh and i - hsh[nums[i]] <= k: 
                return True 
            # Update the index of the current element in the dictionary 
            hsh[nums[i]] = i 
        # If no duplicates found within k distance, return False 
        return False
