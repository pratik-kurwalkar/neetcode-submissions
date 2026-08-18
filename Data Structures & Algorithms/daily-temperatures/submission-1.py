class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        result = [0] * len(t)
        stack = [0]
        for x in range(1, len(t)):
            while len(stack) > 0 and t[x] > t[stack[-1]]:
                result[stack[-1]] = x - stack[-1]
                stack.pop()
            stack.append(x)
        return result    
    
