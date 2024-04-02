#Solution 1
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {'+','-','*','/'}
        for c in tokens:
            if c in op:
                first = int(stack.pop())
                second = int(stack.pop())
                if c == '+':
                    res = second + first
                elif c == '-':
                    res = second - first
                elif c== '*':
                    res = second * first
                elif c == '/':
                    res = int(second / first)
                stack.append(res)
            else: 
                stack.append(c)
        return int(stack[0])

#Solution 2
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]
