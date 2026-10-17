class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        hMap = {} 
        res = []
        n = len(nums2)

        for i in range(n-1, -1, -1):  # move right to left through nums2

            while stack and nums2[i] > stack[-1]: # loop until the new number is greater than the tail if the stack
                stack.pop()

            if stack: # after removing smaller values, top is the next greater element
                hMap[nums2[i]] = stack[-1]
            else: # no greater element exists to the right, assign with -1
                hMap[nums2[i]] = -1

            stack.append(nums2[i]) # add the number to the stack.
        
        for i in range(len(nums1)):
            res.append(hMap[nums1[i]])
        
        return res
# TC: O(n) - runs for n number of times depending on nums1 and nums2's length

# SC: O(n) - dictionaries for storing the nums2 values. Worse case, the length is n. Also has lists but it's sc is O(1) so ignored