class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for each in tokens:
            if each in ["+", "-", "*", "/"]:
                left = int(stack[-2])
                right = int(stack[-1])
                
                if each == "+":
                    result = left + right
                elif each == "-":
                    result = left - right
                elif each == "*":
                    result = left * right
                else: 
                    result = left / right
                
                stack.pop() 
                stack.pop()
                stack.append(int(result))
            
            else:
                stack.append(int(each))
        return stack[-1]
