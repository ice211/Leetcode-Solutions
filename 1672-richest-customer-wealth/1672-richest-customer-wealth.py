class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maxWealth =  0 
        for each in accounts:
            total = 0 #total needs to be 0 for every new set
            for wealth in each:
                total += wealth
            if total > maxWealth:
                maxWealth = total
        return maxWealth

#TC:O(m × n); number of rows x number of columns
#SC: O(1); just storing the max wealth and total