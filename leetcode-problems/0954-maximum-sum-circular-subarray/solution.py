class Solution(object):
    def maxSubarraySumCircular(self, nums):
        tot = sum(nums)
        c = m = left_sum = max_prefix_sum = nums[0]
        for i, num in enumerate(nums[1:]):
            c = max(c + num, num)
            m = max(m, c, max_prefix_sum + tot - left_sum)
            left_sum += num
            max_prefix_sum = max(max_prefix_sum, left_sum)
        
        # Handle the case where all elements are negative
        if m == 0 and all(x < 0 for x in nums):
            return max(nums)
        
        return m
