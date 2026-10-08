class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0: #check for empty list
            return 0

        numSet = set(nums)
        lengths = [0] # intial value 0 to have something to campare for the maxLength
        for each in numSet:
            if (each-1) in numSet: # finding the head number. If it does not have a left neighbor, it's the head
                continue

            else:
                count = 0 # 0 as we need to count length for each head
                start = each 
                while (start + 1) in numSet: #loop until there is a right neighbor
                    count += 1
                    start += 1
            lengths.append(count)
        maxLength = max(lengths)+1            
        return maxLength

# TC: O(n) — each number is processed at most a constant number of times using O(1) average HashSet lookups.
# SC: O(n) — the HashSet and lengths list can each store up to n elements.