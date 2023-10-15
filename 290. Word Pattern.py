class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic={}
        dic1={}
        idx=0
        words=s.split()
        if len(pattern)!=len(words):
            return False
        for ch in pattern:
            if ch not in dic:
                if words[idx] in dic1:
                    return False
                dic[ch]=words[idx]
                dic1[words[idx]]=ch
            else:
                if dic[ch] != words[idx] :
                    return False
            idx+=1
        return True