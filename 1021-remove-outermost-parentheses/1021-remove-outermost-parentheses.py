class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        result = []

        for each in s:
            if stack: # if the stack already has something, it is not an outer parenthesis
                if each == "(": #  stack is already non-empty, so this is an inner opening parenthesis
                    stack.append(each)
                    result.append(each)
                else:
                    stack.pop() #if it is a closing bracket, pop it from the stack
                    if stack: # but be careful as it can be the outermost bracket. If popping the stack makes the stack empty, it is outer bracket. if there is still something in the stack, we are good and will append it in the result.
                        result.append(")")
            else: # if the stack is empty when each is passed, it is an outer bracket. We add it to the stack for the process but do not add it to the result.
                stack.append(each)

        return "".join(result)

# TC: O(n) one for loop that runs for n times where n is the length of the input s
# SC: O(n) for the stack and the result which can store at most n characters