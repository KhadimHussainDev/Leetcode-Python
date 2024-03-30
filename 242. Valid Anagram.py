#Solution 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=sorted(s)
        t=sorted(t)
        return s==t

#Solution 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dic = {}
        for x in s:
            if dic.get(x) is None:
                dic[x] = 0
            dic[x] = dic[x] + 1
        for x in t:
            if dic.get(x) is None:
                return False
            dic[x] = dic[x] - 1
        for x, y in dic.items():
            if y > 0:
                return False
        return True
    
#Solution 3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        for x in s:
            if t.find(x)==-1:
                return False
            t=t.replace(x,' ',1)
        return len(s)==len(t)
        