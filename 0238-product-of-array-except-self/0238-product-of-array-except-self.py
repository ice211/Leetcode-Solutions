class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left, right = 1, 1 
        final = []
        leftPass = [1] * len(nums)
        rightPass = [1] * len(nums)
    
        for i in range(len(nums)):
            leftPass[i] = left
            left *= nums[i] 

        for i in range(len(nums)-1,-1,-1):
            rightPass[i] = right
            right *= nums[i]

        for i in range(len(nums)):
            final.append(leftPass[i] * rightPass[i])
        return final
