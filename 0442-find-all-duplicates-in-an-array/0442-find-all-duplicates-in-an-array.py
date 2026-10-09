class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        final = []
        if len(nums)<=1:
            return final 

        for i in range(len(nums)):
            absNum = abs(nums[i]) - 1
            if nums[absNum] < 0:
                final.append(abs(nums[i]))
            else:
                nums[absNum] = nums[absNum] * (-1)
        return final

        
        
            
        