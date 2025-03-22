class Solution: 
    def minSubArrayLen(self, target, nums): 
        ans = float('inf') 
        curr = 0 
        l = 0 
        for r in range(len(nums)): 
            curr += nums[r] 
            while curr >= target: 
                ans = min(ans, r - l + 1) 
                curr -= nums[l] 
                l += 1 
        return ans if ans != float('inf') else 0
