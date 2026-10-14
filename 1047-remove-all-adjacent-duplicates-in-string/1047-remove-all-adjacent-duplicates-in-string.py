class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for each in s:    
            if stack and stack[-1] == each:
                stack.pop()
            else:
                stack.append(each)
        return "".join(stack)