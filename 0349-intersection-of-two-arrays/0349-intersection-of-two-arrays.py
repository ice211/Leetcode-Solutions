class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        Output = [] #Output list to store the final output
        set1 = set(nums1) #making them a set in order to remove duplication
        set2 = set(nums2)

        for num in set1: #taking each element in set1 as "num"
            if num in set2: #checking if the element is in set2
                Output.append(num) #if num is in set2, it means it is  in botht the arrays and it is an intersection
        
        return Output