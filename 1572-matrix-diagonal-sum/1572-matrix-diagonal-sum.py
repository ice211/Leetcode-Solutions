class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:

        totalLeft, totalRight, final  = 0, 0, 0

        for i in range (len(mat)):
            totalLeft += mat[i][i]
            totalRight += mat[i][len(mat) -1 -i]
        final = totalRight + totalLeft

        if len(mat) % 2 == 1:
            center = mat[len(mat) // 2][len(mat) // 2]
            final = final - center
        
        return final
            