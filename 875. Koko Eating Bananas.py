#Solution 1
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left , right = 1 , max(piles)
        res = right

        while left <= right :
            mid = (left + right) >> 1
            total = 0
            for p in piles :
                total += math.ceil(p / mid) 
            
            if total <= h:
                res = min(res , mid)
                right = mid - 1
            else :
                left = mid + 1 
        return res