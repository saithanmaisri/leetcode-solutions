class Solution(object): 
    def threeSum(self, nums): 
        i = 0 
        n = len(nums) 
        s = set() 
        lkp = {} 
        while i < n: 
            j = i + 1 
            while j < n: 
                k = -(nums[i] + nums[j]) 
                if k in lkp: 
                    temp = [nums[i], nums[j], k] 
                    temp.sort() 
                    s.add(tuple(temp)) 
                if k not in lkp: 
                    lkp[nums[j]] = k 
                j = j + 1 
            if j == n: 
                lkp.clear() 
                i = i + 1 
        return list(s)
