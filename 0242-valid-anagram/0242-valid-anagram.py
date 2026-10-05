class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = {} #initializing the dictionary
        
        for each in s: #counting the instance of each character in the string
            dictionary[each] = dictionary.get(each,0)+1 #for first instance, first add the character-key in the dictionary and then assign 1 as it's value
        
        for each in t: 
            if each not in dictionary: #if even one character is off, it's invalid
                return False
            else: #decrease from dictionary with each instance in t
                dictionary[each] -= 1
        
        for key, val in dictionary.items():
            if val != 0: 
                return False

        return True 

#TC: O(m+n); 2 independent loops -> O(n)
#SC: O(1); Under this problem’s fixed 26-letter alphabet constraint, it simplifies to O(1).