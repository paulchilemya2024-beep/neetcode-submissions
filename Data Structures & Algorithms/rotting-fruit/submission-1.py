class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time,fresh = 0,0
        ROWS,COLS = len(grid),len(grid[0])
        queue = collections.deque([])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append([r,c])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        while queue and fresh >0:
            n = len(queue)

            for i in range(n):
                r,c = queue.popleft()
                for dr,dc in directions:
                    R,C = r+dr, c+dc
                    if 0<=R<ROWS and 0<=C<COLS:
                        if grid[R][C] == 1:
                            grid[R][C]=2
                            fresh -= 1
                            queue.append([R,C])
            time += 1
        return time if fresh ==0 else -1
        