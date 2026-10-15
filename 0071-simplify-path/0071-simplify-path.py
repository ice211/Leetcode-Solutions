class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        components = path.split('/')

        for each in components:
            if each == '..':
                if stack:
                    stack.pop()
            elif each not in ['','.']:
                stack.append(each)
        return '/' + '/'.join(stack)        
 # TC: O(n) - one independent for loop. split() and join() are also O(n)
 # SC: O(n) - one stack that stores at most n input