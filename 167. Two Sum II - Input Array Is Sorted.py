#Solution 1
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start=0
        end=len(numbers)-1
        
        while start < end:
            curSum=numbers[start]+numbers[end]
            if curSum < target:
                start += 1
            elif curSum > target:
                end -= 1
            else:
                return [start+1,end+1]
            
#Solution 2
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left,right=0,len(numbers)-1
            while left<=right:
                mid=(left+right)//2
                n=numbers[i]+numbers[mid]
                if n==target:
                    if i+1==mid+1:
                        return i+1,mid+2
                    return i+1,mid+1
                if n<target:
                    left=mid+1
                else:
                    right=mid-1
        