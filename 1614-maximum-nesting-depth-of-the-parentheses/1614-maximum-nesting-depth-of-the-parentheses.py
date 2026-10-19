class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxi, counter = 0, 0

        for each in s:
            if each == "(":
                stack.append(each)
                counter += 1
            elif each  == ")":
                stack.pop()
                maxi = max(maxi, counter)
                counter -= 1
        return maxi

