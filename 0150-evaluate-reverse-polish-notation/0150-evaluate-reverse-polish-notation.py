class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for each in tokens:
            if each in ["+", "-", "*", "/"]: # this checks for operators. The operators are only there if there are at least 2 numbers before them
                left = int(stack[-2]) # input string -> int for calculation
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
                stack.append(int(result)) # remember the int because the question wants the division towards 0.
                # -5//2 -> -3     int(-5/2) -> -2 
            
            else:
                stack.append(int(each)) #if there is only number without operation
        return stack[-1]
# TC: O(n) — you go through all n tokens once, and each stack operation is O(1).
# SC: O(n) — in the worst case, the stack can grow with the number of tokens.