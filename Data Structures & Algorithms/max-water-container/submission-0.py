class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #input [3, 1, 3] output = [3X2= 6]
        res = 0

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                mxheight = min(heights[i], heights[j])
                width = j - i

                area = mxheight * width
                res = max(res, area)

        return res