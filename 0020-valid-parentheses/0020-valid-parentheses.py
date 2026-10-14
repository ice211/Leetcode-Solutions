class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []

        for each in s:
            if each in pairs:
                stack.append(each)

            if each not in pairs:
                if len(stack) == 0:
                    return False

                if pairs[stack[-1]] == each:
                    stack.pop()
                    continue

                elif pairs[stack[-1]] != each:
                    return False
                
        if len(stack) == 0:
            return True
        else:
            return False
      


