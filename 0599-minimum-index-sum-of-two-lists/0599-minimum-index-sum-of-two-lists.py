class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        list1Dict = {}
        result = []
        bestSum = float('inf')

        for i in range(len(list1)):
            list1Dict[list1[i]] = i
        
        for j in range(len(list2)):
            if list2[j] in list1Dict:
                sum = list1Dict[list2[j]] + j

                if sum < bestSum:
                    bestSum = sum
                    result = [list2[j]] 

                elif sum == bestSum:
                    result.append(list2[j])

        return result
                    

                
                
                
                

        