class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort() # sort the list so the pointers can be predictible

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]: # to avoid duplication. [-1, -1, 2]
                continue

            l = i+1 # l starts one step to the right of i
            r = len(nums)-1 

            while l<r: 
                currentSum = nums[i] + nums[l] + nums[r] # first find the sums with the current pointers
                if currentSum < 0:
                    l += 1 # in this case we need a greater number to make it a 0 so moving l + 1
                elif currentSum > 0:
                    r -= 1 # in this case we need a smaller number to make it a 0 so moving r - 1
                else:
                    result.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1 # avoid duplicate l
                
        return result
# TC: O(n2) nested loop. while loop runs again for each i
# SC: O(1) auxiliary space, excluding sorting/output