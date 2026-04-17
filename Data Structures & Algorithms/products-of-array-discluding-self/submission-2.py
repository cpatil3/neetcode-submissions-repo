class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        zero_cnt, prod = 0, 1

        for n in nums:
            if n:
                prod *= n
            else:
                zero_cnt += 1
        if zero_cnt > 1: return [0] * len(nums)
        
        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt: res[i] = 0 if c else prod
            else: res[i] = prod // c
        
        return res
