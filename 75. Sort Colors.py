#Solution 1
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0 = 0
        count1 = 0
        count2 = 0
        
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 +=1
        
        for i in range(len(nums)):
            if count0 > 0:
                count0 -=1
                nums[i] = 0
            elif count1 > 0:
                count1 -= 1
                nums[i] = 1
            else:
                nums[i] = 2
        
#Solution 2 (With one pass)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left , right , idx = 0 , len(nums) - 1 , 0
        while idx <= right:
            if nums[idx] == 0 :
                nums[left] , nums[idx] = nums[idx] , nums[left]
                left += 1
                idx +=1
            elif nums[idx] == 1:
                idx += 1
            else:
                nums[right] , nums[idx] = nums[idx] , nums[right]
                right -= 1