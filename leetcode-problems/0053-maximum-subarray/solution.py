class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        max1 = nums[0]
        sum1 = nums[0]
        for i in range(1, n):
            if sum1 < 0:
                sum1 = 0
            sum1 += nums[i]
            max1 = max(max1, sum1)
        
        # If all numbers are negative, return the largest negative number
        if max1 < 0 and all(num < 0 for num in nums):
            return max(nums)
        
        return max1
