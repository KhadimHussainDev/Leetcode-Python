# Solution 1
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        close = 10000000
        minDiff = 10000000 

        for i,num in enumerate(nums):


            l = i + 1
            r = len(nums) - 1

            while l < r :
                sum = num + nums[l] + nums[r]
                diff = abs(sum-target)
                if diff < minDiff :
                    close = sum
                    minDiff = diff
                

                if sum < target :
                    l +=1
                elif sum > target :
                    r -= 1
                else:
                    return sum
        return close
        
# Solution 2
