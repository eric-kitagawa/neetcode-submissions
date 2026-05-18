class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowmap = {}
        colmap = {}
        sqmap = {}
        for i in range(len(board)):
            rowmap[i] = set()
            for j in range(len(board[i])):
                sqkey = (i // 3, j // 3)
                if sqkey not in sqmap:
                    sqmap[sqkey] = set()

                if j not in colmap:
                    colmap[j] = set()

                col = board[i][j]
                if col in rowmap[i] or col in colmap[j] or col in sqmap[sqkey]:
                    return False

                if col != ".":
                    rowmap[i].add(col)
                    colmap[j].add(col)
                    sqmap[sqkey].add(col)

        return True