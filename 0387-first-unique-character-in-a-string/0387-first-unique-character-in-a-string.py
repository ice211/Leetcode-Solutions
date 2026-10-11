class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {} # initializing the dictionary 

        for each in s:
            counter[each] = counter.get(each, 0)+1 # counting each character's count 
        
        for i in range(len(s)):
            if counter[s[i]] == 1: # check first key that has a value 1
                return i # this returns the i on first match
        return -1 # if no match, return -1

# TC: O(n) - loops 2 independent times for the length of s
# SC: O(n) - because s contains only lowercase English letters, so your dictionary can have at most 26 keys.