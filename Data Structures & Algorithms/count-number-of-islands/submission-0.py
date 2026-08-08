class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visit = set()

        def bfs(r,c):
            q = collections.deque([])
            visit.add((r,c))
            q.append([r,c])

            while q:
                r,c = q.popleft()
                directions = [[0,1],[1,0],[-1,0],[0,-1]]
                
                for dr,dc in directions:
                    ROW, COL = r+dr,c+dc

                    if (ROW in range(ROWS) and COL in range(COLS) 
                    and (ROW,COL) not in visit and grid[ROW]
                    [COL]=="1"):
                        visit.add((ROW,COL))
                        q.append([ROW,COL])

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] =="1":
                    bfs(r,c)
                    islands +=1
        return islands
                

        
        