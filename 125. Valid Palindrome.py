#Solution 1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()

        st=""
        for ch in s:
            if (ch >='a' and ch<='z') or (ch>='0' and ch<='9'):
                st+=ch
        
        start=0
        end=len(st)-1

        while start<end:
            if st[start]!=st[end]:
                return False
            start+=1
            end-=1
        return True
        

#Solution 2
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left=0
        right=len(s)-1
        while left < right:
            while left<right and not self.alphaNum(s[left]):
                left+=1
            while right>left and not self.alphaNum(s[right]):
                right-=1

            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True
    def alphaNum(self,ch):
        if (ch >='a' and ch<='z') or (ch>='0' and ch<='9') or (ch >='A' and ch<='Z'):
            return True
        return False