class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0 # start l at the front
        r = len(height) - 1 # start r from the end
        answer = 0

        while l < r:
            width = r - l # this gives the width of l and r
            validHeight = min(height[l], height[r]) # we need to take the min. height because if we take the max., the water will overflow from the min.
            area = validHeight * width
            answer = max(answer, area) # we only need the max. area

            if height[l]<height[r]: # left side is limiting the area, so move it inward to look for a taller wall
                l += 1
            elif height[r]<height[l]: # see not above
                r -= 1
            else: #if height of both l and r are same, change any and the code will adjust it in the next loop
                l += 1

        return answer
# TC : O(n) - independent while loop for n no. of input
# SC : O(1) - fixed number of variables regardless of input size
            
