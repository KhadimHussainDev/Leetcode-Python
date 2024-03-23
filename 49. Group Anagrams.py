#Solution 1
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for i in range(0,len(strs)):
            x=''.join(sorted(strs[i]))
            dic[x].append(strs[i])
            
        return dic.values()
            
