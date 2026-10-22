class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        hMap = {}
        count = 0

        for i in range(len(word)):
            if word[i] in hMap and ord(word[i]) < 91:
                continue
            else:
                hMap[word[i]] = i
            
        for key, val in hMap.items():
            if key.upper() in hMap and hMap[key.upper()] > hMap[key]:
                count += 1
        
        return count
