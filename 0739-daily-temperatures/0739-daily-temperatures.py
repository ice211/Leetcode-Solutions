class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        n = len(temperatures)
        result = [0] * n
        
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stack_temp, stack_index = stack.pop()
                result[stack_index] = i - stack_index
            stack.append((t , i))
        return result

                    