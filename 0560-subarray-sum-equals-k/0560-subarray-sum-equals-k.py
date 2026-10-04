class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum,count = 0,0 #count gives the count of final subarrays 
        prefixSumDict = {0:1} #before we read any numbers, we pretend we have already seen a prefix sum of 0 once. 

        for num in nums:
            prefixSum += num
            needed = prefixSum - k #what earlier prefix sum we need to have seen so the difference equals k

            if needed in prefixSumDict: #if the earlier prefix sum exists, add how many times we have seen it
                count += prefixSumDict[needed]

            prefixSumDict[prefixSum] = prefixSumDict.get(prefixSum, 0)+1 #also add the prefixSum to the dict. for future
        return count
#TC: O(n); one pass through nums
#SC: O(n); prefixSumDict can store up to n different prefix sums; O(1) for other vars


