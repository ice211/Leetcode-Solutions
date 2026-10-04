class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        
        hMap = {}

        for first in nums1: #take each integer from nums1
            for second in nums2: #take each integer from nums2
                total = first + second  #add them
                hMap[total] = hMap.get(total,0)+1 #count the instance of each total in a dictionary
        
        count = 0
        for third in nums3:
            for fourth in nums4:
                needed = - (third + fourth) #this will tell us what we need for the total to be 0
                
                if needed in hMap:
                    count += hMap[needed]

        return count
