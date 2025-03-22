class Solution(object): 
    def rotate(self, nums, k): 
        k = k % len(nums) 
        nums2 = nums[-k:] + nums[:-k] 
        for i in range(len(nums)): 
            nums[i] = nums2[i] 
