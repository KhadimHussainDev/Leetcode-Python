#Solution 1
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        
        if nums[0] > 0:
            return res

        for i,num in enumerate(nums):
            if i > 0 and nums[i-1] == num:
                continue

            l = i+1
            r = len(nums)-1

            while l < r :
                sum = num + nums[l] + nums[r]
                if sum == 0:
                    res.append([num,nums[l],nums[r]])
                    l += 1
                    r -+ 1
                elif sum < 0:
                    l += 1
                else: 
                    r -= 1
        # To remove duplicates
        res = list(res for res,_ in itertools.groupby(res))
        return res

#Solution 2
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        
        if nums[0] > 0:
            return res

        for i,num in enumerate(nums):
            if i > 0 and nums[i-1] == num:
                continue

            l = i+1
            r = len(nums)-1

            while l < r :
                sum = num + nums[l] + nums[r]
                if sum == 0:
                    res.append([num,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    # To avoid Duplicates
                    while nums[l]==nums[l-1] and l < r:
                        l += 1
                elif sum < 0:
                    l += 1
                else: 
                    r -= 1
        return res

#Solution 3
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        for i,num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and nums[i-1] == num:
                continue

            l = i+1
            r = len(nums)-1

            while l < r :
                sum = num + nums[l] + nums[r]
                if sum == 0:
                    res.append([num,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while nums[l]==nums[l-1] and l < r:
                        l += 1
                elif sum < 0:
                    l += 1
                else: 
                    r -= 1
        return res
