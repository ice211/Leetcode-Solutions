class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for i in range(len(num)):
            while stack and k > 0 and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
        
        if k>0:
            for i in range(k):
                stack.pop()
    
        result = "".join(stack)
        result = result.lstrip('0')

        if len(result) == 0:
            return "0"

        return result
    