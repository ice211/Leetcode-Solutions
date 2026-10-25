class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for each in asteroids:
            while stack and stack[-1] > 0 and each < 0: #the asteroid wont collide if the tail is negative and each is positive

                if abs(each) > stack[-1]:
                    stack.pop()
                #if current asteroid is bigger, we need to pop the stack. but we need to keep running it to check with the stack deeper 

                elif abs(each) == stack[-1]:
                    stack.pop()
                    break
                #nothing gets added if the stack and current is same. both explode

                else:
                    break
                # this is when the current asteroid is smaller, the stack remains same


            else:
                stack.append(each) 
                # only runs if the while loop runs without hitting break.

        return stack
                

            

