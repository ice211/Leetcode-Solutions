class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = []

        nums1Set = set(nums1) #remove duplication and arrancge in asc
        nums2Set = set(nums2)

        for n in nums1Set: #take each number nums1Set and put it in n
            if n in nums2Set: #Does nums2Set contain this number n?
                result.append(n) #if the n matches, add that to result

        return result 