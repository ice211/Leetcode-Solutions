class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {} #initializing the dictionary

        for each in magazine: #counting the instance of each character in magazine
            count[each] = count.get(each, 0) + 1
        
        for each in ransomNote: 
            if each not in count: # if a ransomNote character does not exist in magazine
                return False 
            
            if count[each] == 0: #if the ransomNote has a char and magazine does not/it's 0
                return False

            count[each] -= 1 #passing the above 2 means the char from ransomnote is in magazine. deduct one instance
        
        return True
        

# TC: O(m + n)
# m = len(magazine), n = len(ransomNote) We traverse each string once.

# SC: O(m), because the dictionary could contain up to m distinct characters.