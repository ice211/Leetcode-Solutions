class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # if the key does not exist, Python automatically creates an empty set if we use defaultdict. 
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9): #hard coded as it can only have 9 rows and columns
            for c in range(9):
                if board[r][c] == ".": # ignore "."
                    continue
                
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3 , c // 3)]):# check with each row, column and box.
                # integer division by 3 groups rows and columns into 0, 1, or 2
                # example: rows 0-2 -> 0, rows 3-5 -> 1, rows 6-8 -> 2
                    return False

                cols[c].add(board[r][c]) #if not present add in the respective hashmap for cols, rows or squares
                rows[r].add(board[r][c])
                squares[(r // 3 , c // 3)].add(board[r][c])

        return True

# TC: O(m x n) for each value of m and n. The lookup avg. is O(1)
# SC: O(m x n) rows, cols, and squares all store board values