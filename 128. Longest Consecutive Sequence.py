#Solution 1
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic={}
        longest=0

        for num in nums:
            dic[num]=True
        
        for num in dic.keys():
            if dic.get(num-1) is None:
                length=1
                while dic.get(num+length) is not None:
                    length+=1
                longest=max(length,longest)

        return longest


#Solution 2
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        longest=0

        for num in numSet:
            if num-1 not in numSet:
                length=1
                while num+length in numSet:
                    length+=1
                longest=max(longest,length)

        return longest