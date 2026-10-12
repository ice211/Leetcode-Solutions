class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        hMap = {}

        for char in s: 
            hMap[char] = hMap.get(char, 0)+1 
        
        counter = set(hMap.values())
    
        if len(counter)>1:
            return False

        return True
# TC: O(n) one independent loop
# SC: Because s only contains lowercase English letters, so  dictionary can have at most 26 keys