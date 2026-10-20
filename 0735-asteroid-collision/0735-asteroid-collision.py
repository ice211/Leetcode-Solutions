class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for i in range(len(asteroids)):
            alive = True
            while stack and stack[-1] > 0 and asteroids[i] < 0:
                if abs(asteroids[i]) > stack[-1]:
                    stack.pop()

                elif abs(asteroids[i]) == stack[-1]:
                    stack.pop()
                    alive = False
                    break
                else: # abs(each) < stack[-1]:
                    alive = False
                    break   
            if alive:
                stack.append(asteroids[i])       
                
        return stack

