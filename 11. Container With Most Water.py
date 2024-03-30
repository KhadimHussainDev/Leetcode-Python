#Solution 1
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l , r = 0 , len(height) - 1
        while l < r :
            lh = height[l]
            rh = height[r]

            if lh < rh :
                a = lh * (r - l)
                l += 1
            else :
                a = rh * (r - l)
                r -= 1
            area = max(area , a)
        return area
