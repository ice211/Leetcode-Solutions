class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        hMap = {}
        count = 0

        for each in word:
            hMap[each] = hMap.get(each,0)+1
        
        for key,val in hMap.items():
            character = key
            aVal = ord(character)
            needed = aVal - 32
            if chr(needed) in hMap:
                count += 1

        return count
