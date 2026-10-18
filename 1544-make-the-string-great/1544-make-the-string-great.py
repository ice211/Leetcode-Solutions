class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for each in s:
            if stack and abs(ord(each) - ord(stack[-1]))==32:
                stack.pop()
                continue
            else:
                stack.append(each)
        return "".join(stack)
