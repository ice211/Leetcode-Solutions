class Solution:
    def trap(self, height: list[int]) -> int:
        l , r = 0, len(height)-1
        result = 0
        lMax , rMax = 0, 0

        while l<r:
            lMax = max(lMax, height[l]) # tallest wall from each side
            rMax = max(rMax, height[r])

            if lMax < rMax: # water can only be fill until the smaller max as if more than that it will overflow
                capacity = lMax - height[l] # how much water can be filled is determined by the diff. between the min-l or r and subtracting the height.
                result += capacity
                l += 1
            
            else:
                capacity = rMax - height[r]
                result += capacity
                r -= 1
        return result

# TC: O(n) - one independent loop dependent on the length of input
# SC: O(1) - just some variable saves