class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        for each in pushed:
            stack.append(each)

            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        
        if not stack:
            return True
        else:
            return False
