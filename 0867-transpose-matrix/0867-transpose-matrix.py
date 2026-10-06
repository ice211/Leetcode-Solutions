class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        result = [] #to store the final 2-d array
        for i in range(len(matrix[0])): # original columns become result rows
            newRow = [] #a new matrix for each loop
            for j in range(len(matrix)): # go through every original row
                newRow.append(matrix[j][i]) #position is the swapped for row/column
            result.append(newRow)
        return result

#tc: O(n x m) visit every cell in the matrix once
#sc: O(n x m) store every element of the original matrix in a new wd list


