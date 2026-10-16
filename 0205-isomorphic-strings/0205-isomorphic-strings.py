class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictST = {}
        dictTS = {}

        for i in range(len(s)):
            if s[i] not in dictST: # if the input not in dictionary add it and assign a 't' value to it
                dictST[s[i]] = t[i]
            if s[i] in dictST and dictST[s[i]] != t[i]: # if it is already in the dictionary, it needs to be the same as the t value if not, it's false
                return False
        
        for i in range(len(t)):
            if t[i] not in dictTS:
                dictTS[t[i]] = s[i]
            if t[i] in dictTS and dictTS[t[i]] != s[i]:
                return False
        return True
# TC: O(n) 2 individual for loops but lengths are same.
# SC: O(n) have created dictionaries that can store n length inputs.