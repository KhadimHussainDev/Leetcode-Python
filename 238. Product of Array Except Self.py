#Solution 1
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res=[1]*len(nums)
        for i in range(1,len(nums)):
            res[i]=res[i-1]*nums[i-1]
        post=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=post
            post*=nums[i]
        return res

        
#Solution 2
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul=1
        index=-1
        count=0
        for i,num in enumerate(nums):
            if num != 0:
                mul*=num
            else:
                count+=1
                if count==1:
                    index=i
        
        res=[0]*len(nums)
        if count>1:
            return res
        
        if count==1:
            res[index]=mul
            return res
        
        for i,num in enumerate(nums):
            res[i]=mul//num
        return res
        