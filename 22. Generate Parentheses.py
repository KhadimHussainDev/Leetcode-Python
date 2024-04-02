#Solution 1
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN,closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return

            if openN < n :
                stack.append("(")
                backtrack(openN+1 , closeN)
                stack.pop()

            if closeN < openN :
                stack.append(")")
                backtrack(openN,closeN+1)
                stack.pop()

        backtrack(0,0)
        return res


#Solution 2 (Without Stack)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(openN,closeN,s):
            if openN == closeN == n:
                res.append(s)
                return

            if openN < n :
                backtrack(openN+1 , closeN , s + '(')

            if closeN < openN :
                backtrack(openN , closeN+1 , s + ')')

        backtrack(0,0,"")
        return res
    
#Solution 3 (iterative)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        queue = deque([("",0,0)])

        while queue:
            current_str, open_count , closed_count = queue.popleft()

            if open_count == closed_count == n:
                res.append(current_str)

            if open_count < n:
                queue.append((current_str + '(' , open_count + 1 , closed_count))

            if closed_count < open_count :
                queue.append((current_str + ')' , open_count , closed_count + 1))

        return res
