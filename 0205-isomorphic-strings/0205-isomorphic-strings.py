class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        for i in range(len(s)):
            if s[i] not in mapST and t[i] not in mapTS: # check from both s and t side
                mapST[s[i]] = t[i] # if values not in dictionaries, add them and assign value
                mapTS[t[i]] = s[i]

            if s[i] in mapST and mapST[s[i]] != t[i]: # check if i char in s != char in t
                return False

            if t[i] in mapTS and mapTS[t[i]] != s[i]:# check if i char in t != char in s
                return False

        return True