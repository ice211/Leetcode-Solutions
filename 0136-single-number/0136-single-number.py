class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        hMap = {}

        for char in nums: 
            hMap[char] = hMap.get(char,0)+1
        
        for key,val in hMap.items():
            if val != 2:
                return key

        

