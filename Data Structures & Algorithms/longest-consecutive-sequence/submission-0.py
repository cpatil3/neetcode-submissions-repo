class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in nums:
            streak = 0
            while num in store:
                num +=1
                streak +=1
            
            res = max(res, streak)
        
        return res