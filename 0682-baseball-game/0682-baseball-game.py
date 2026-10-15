class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []

        for each in operations:
            if each == "C":
                stack.pop()

            elif each == "D":
                result = stack[-1] * 2
                stack.append(result)

            elif each == "+":
                result = stack[-1] + stack[-2]
                stack.append(result)

            else:
                stack.append(int(each))

        return sum(stack)