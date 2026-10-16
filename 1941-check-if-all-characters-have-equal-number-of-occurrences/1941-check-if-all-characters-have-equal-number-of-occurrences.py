class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hMap = {}
        
        for each in s:
            hMap[each] = hMap.get(each, 0)+1

        result = set(hMap.values()) # .values() gives the values of the keys in the dictionary

        if len(result) > 1: # as set stores only unique value, it's length more than one mean the character frequency is different
            return False
        else:
            return True

# TC : O(n) one for loop for dictionary filling
# SC : O(1) the dictionary can store at most 26 lowercase alphabets