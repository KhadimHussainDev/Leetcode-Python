#Solution 1
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for i  in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i] :
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res
            
#Solution 2 (with constant memory)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        res = [0]*size
        largest = 0

        for i in range(size-1 , -1 , -1):
            if temperatures[i] >= largest:
                largest = temperatures[i]
                continue
            days = 1
            while temperatures[i + days] <= temperatures[i]:
                days += res[i + days]
            res[i] = days

        return res