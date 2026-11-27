class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        
        hMap = {}
        total = 0
        for i in range(len(nums)): #we are going to fill the values as a set of indices
            if nums[i] in hMap:
                hMap[nums[i]].append(i) #if the key is in the map, append the index as the value
            else:
                hMap[nums[i]] = [i] #if it is the first instance, add the first index

        for key,val in hMap.items():
            count = len(val) #this gets the length of values for each key
            total += count * (count - 1) // 2 #need to calculate the number of pairs and add it as the total

        return total

#TC: O(n) — loop through nums once, then through the hashmap once. O(n) + O(n) = O(n).

#SC: O(n) — hashmap can store up to n indices total, so the extra memory grows with the input. 