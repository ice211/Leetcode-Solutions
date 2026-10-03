class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hMap = {} #declaring the dictionary
 
        for i in range (len(nums)): #looping through each index in the input 
            difference = target - nums[i] #deciding what the required number is 

            if difference in hMap: 
                return [i, hMap[difference]] #return the index along whit the index where the difference is 
            else:
                hMap[nums[i]] = i #if diff. is not in the hMap, add the data along with the index

    