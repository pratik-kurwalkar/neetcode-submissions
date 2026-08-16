class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def checkValidList(x):
            nums = [c for c in x if c != "."]
            return len(set(nums)) == len(nums)

        # Check rows
        for x in board:
            if not checkValidList(x):
                return False
        # Check columns
        for x in range(len(board)):
            column = []
            for y in range(len(board)):
                column.append(board[y][x])
            if not checkValidList(column):
                return False
        
        # Check grid
        for i in range (0, 9, 3):
            for x in range(0, 9, 3):
                grid = []
                for y in range(0, 3):
                    grid.extend([board[x][y+i], board[x+1][y+i], board[x+2][y+i]])
                if not checkValidList(grid):
                    return False
        
        return True