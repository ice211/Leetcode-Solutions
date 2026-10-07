class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        d = {}
        for i in range(len(magazine)):
            if magazine[i] in d:
                d[magazine[i]] += 1
            else:
                d[magazine[i]] = 1
        
        for i in range(len(ransomNote)):
            if ransomNote[i] not in d:
                return False

            if d[ransomNote[i]] == 0:
                return False
        
            d[ransomNote[i]] -= 1


        return True
