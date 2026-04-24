class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #input [3, 1, 3] output = [3X2= 6]
        # [1, 3, 3] 
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)

            if heights[l] <= heights[r]:
                l += 1

            else:
                r -= 1
        return res