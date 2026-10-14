class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for each in s:    
            if stack and stack[-1] == each:
                stack.pop()
            else:
                stack.append(each)
        return "".join(stack)
# TC: O(n) only one independent for loop which loops for n times and .join is O(n) too
# SC : O(n) one stack that increases with n