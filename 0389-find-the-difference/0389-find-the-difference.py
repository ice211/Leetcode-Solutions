class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter = {}

        for each in t: # count the instance of each char in t
            counter[each] = counter.get(each, 0)+1
        
        for char in s: # compare with each char in s and reduce if found
            if char in counter:
                counter[char] -= 1
        
        for key,val in counter.items(): #look for the key with val 1 and return the key
            if val == 1:
                return key
# TC : O(n) - 3 separate linear loops
# SC : O(1) - dictionary can contain at most 26 lowercase letters