class Solution:
    def findLucky(self, arr: list[int]) -> int:
        result = []
        hMap = {}


        for each in arr:
            hMap[each] = hMap.get(each,0)+1

        for key, val in hMap.items():
            if key == val:
                result.append(val)

        if len(result) < 1:
            return -1
        else:
            return max(result)

