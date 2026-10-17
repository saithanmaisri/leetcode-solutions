class Solution(object):
   
    def twoSum(self,nums,target):
        seen={}
        for i in range(len(nums)):
            req=target-nums[i]
            if req in seen:
                return [seen[req],i]
            seen[nums[i]]=i
