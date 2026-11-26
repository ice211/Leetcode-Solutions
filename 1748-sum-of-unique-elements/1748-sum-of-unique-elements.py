class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        hMap = {}
        res = []

        for each in nums:
            hMap[each] = hMap.get(each, 0)+1
        
        for i in range(len(nums)):
            if hMap[nums[i]] == 1:
                res.append(nums[i])
        
        return sum(res)
