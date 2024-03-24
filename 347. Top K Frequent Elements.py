#Solution 1
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        freq=[[] for i in range(len(nums)+1)]
        
        for num in nums:
            dic[num]=1+dic.get(num,0)

        for n,c in dic.items():
            freq[c].append(n)
            
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res

#Solution 2
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for num in nums:
            if dic.get(num) is None:
                dic[num]=0
            dic[num]+=1
        lst=[]
        for x in dic.keys():
            lst.append((dic[x],x))
        lst.sort(reverse=True)
        arr=[]
        for x,y in lst:
            if len(arr)<k:
                arr.append(y)
        return arr