#Solution 1
class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] in "}])" or len(s) % 2 == 1:
            return False
        stack = []
        for ch in s:
            if ch in "{[(" : 
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if not ((ch == ')' and top == '(') or (ch == '}' and top == '{') or  (ch == ']' and top == '[')):
                    return False
        return len(stack) == 0
    
#Solution 2
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(' , '}':'{' , ']':'['}
        stack = []

        for ch in s :
            if ch not in dic :
                stack.append(ch)
                continue
            if not stack or stack[-1] != dic[ch]:
                return False
            stack.pop()

        return not stack


