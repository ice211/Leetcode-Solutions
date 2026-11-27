class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        hMap1, hMap2 = {}, {} #made 2 hashmaps. Cnot not use the sub method becasue words2 may have words that are not in words1
        output = 0
 
        for each in words1: #count the number in words1
            hMap1[each] = hMap1.get(each,0)+1 
        
        for each in words2: #count the number in words2
            hMap2[each] = hMap2.get(each,0)+1 
        
        for key,val in hMap1.items(): 
            if val == 1: #useless if val > 1
                if key in hMap2 and hMap2[key]==1: #check for common key with occurance 1
                    output += 1
        
        return output

#tc: O(n+ m) we loop through words1, words2, and then at most all keys from words1.
#sc: O(n+m) two hashmaps can grow with both inputs