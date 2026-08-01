class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        Drows = defaultdict(set)
        Dcols = defaultdict(set)
        Dsquare = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in Drows[i] or board[i][j] in Dcols[j] or board[i][j] in Dsquare[(i//3,j//3)]:
                    return False
                
                Drows[i].add(board[i][j])
                Dcols[j].add(board[i][j])
                Dsquare[(i//3, j//3)].add(board[i][j])

        return True

        