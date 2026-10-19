class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        result = []

        for each in s:
            if not stack:
                if each == "(":
                    stack.append(each)
                else:
                    stack.pop()

            else:
                if each == "(":
                    stack.append(each)
                    result.append("(")
                else:
                    stack.pop()
                    if stack:
                        result.append(")")
                    
        return "".join(result)