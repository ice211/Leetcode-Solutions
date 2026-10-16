class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        dicti = {}
        result = []
        for each in nums1:
            dicti[each] = dicti.get(each,0)+1
        
        for i in range(len(nums2)):
            if nums2[i] in dicti and dicti[nums2[i]]>0:
                result.append(nums2[i])
                dicti[nums2[i]] -= 1

        return result


            