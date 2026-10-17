class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        hMap = {} 
        res = []
        n = len(nums2)

        for i in range(n-1, -1, -1):
            while stack and nums2[i] > stack[-1]:
                stack.pop()
            if stack:
                hMap[nums2[i]] = stack[-1]
            else:
                hMap[nums2[i]] = -1

            stack.append(nums2[i])
        
        for i in range(len(nums1)):
            res.append(hMap[nums1[i]])
        
        return res