#Solution 1
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        stack = []
        for i in range(len(position)):
            pair.append((position[i],speed[i]))
        pair.sort()
        while pair :
            pos , sp = pair.pop()
            completion_time = (target - pos) / sp
            stack.append(completion_time)
            if len(stack) > 1 and stack[-1] <= stack[-2] :
                stack.pop()
        return len(stack)
    
#Solution 2