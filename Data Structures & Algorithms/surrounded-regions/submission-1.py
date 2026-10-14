class Solution:
    def solve(self, board: List[List[str]]) -> None:
       
        #move horizontally or vertically
        #region is formed by connection every "O" cell
        #a region is surrounded if none of the "O" cell are on the edge of the board
        #Capture evrything apart from the unsurrounded region

        #Determine unsurronded region


        ROWS, COLS = len(board), len(board[0])
        uns_coor = set()
    
        def capture(r,c):
            if r <0 or c<0 or r==ROWS or c == COLS or board[r][c] != "O" or (r,c) in uns_coor:
                return 
            uns_coor.add((r,c))
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r, c-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0,ROWS-1] or c in [0, COLS-1]):
                    capture(r,c)
        #Use a for loop to capture everything apart from the surrounded region
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in uns_coor and board[r][c] == "O":
                    board[r][c] = "X"

                


        
        