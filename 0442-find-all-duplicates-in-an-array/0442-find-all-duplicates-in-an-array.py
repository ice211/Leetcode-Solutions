class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        result = []

        if len(nums) < 1:
            return result
        
        for i in range(len(nums)):
            markerIndex = abs(nums[i]) - 1
            if nums[markerIndex] < 0:
                result.append(abs(nums[i]))
            else:
                nums[markerIndex] = nums[markerIndex] * (-1)
        return result