class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        n = len(heights)
        res = [0] * n
        stack = []

        stack.append(heights[n-1]) 

        for i in range(n-2,-1,-1):
            count = 0
            while stack and stack[-1] < heights[i]:
                stack.pop()
                count += 1
            if stack:
                count += 1
                
            res[i] = count 
            stack.append(heights[i])
        return res
            