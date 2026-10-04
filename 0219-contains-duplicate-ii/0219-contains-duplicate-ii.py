class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dictionary = {} #dictionary initialization

        for i in range(len(nums)):
            if nums[i] in dictionary: #check if the key is in the dictionary
                if i-dictionary[nums[i]] <=k:#check if i-j <= k 
                    return True
            dictionary[nums[i]] = i #need the most recent index for each key in the dictionary

        return False #if no satisfaction, return false 

#TC: O(n); only loops through nums once
#SC: O(n) for the dictionary