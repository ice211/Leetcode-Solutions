class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        res = [0]*len(temperatures)

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                old_temp, old_index = stack.pop()
                res[old_index] = i - old_index
            stack.append((temperatures[i], i))
        return res