class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hMap = {}

        for i in range (len(nums)):
            difference = target - nums[i]

            if difference in hMap:
                return [i, hMap[difference]]
            else:
                hMap[nums[i]] = i

    