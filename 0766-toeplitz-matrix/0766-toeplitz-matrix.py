class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        for i in range(len(matrix) - 1):
            for j in  range(len(matrix[0]) - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False #dont do a == a = True because it gives true even if one condition satisfies
        return True


 # the idea is that for checking Toeplitz, we need to check for diagonal numbers
 # so we checked i and j with its 1 increment values.

 # TC: O(nxm) checking essentially every cell in the matrix once, comparing it with its down-right neighbor.
 # SC: O(1) just comparing, nothing created.