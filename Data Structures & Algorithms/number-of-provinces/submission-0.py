class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n))
        rank = [1] *n

        def find(x: int) -> int:
            res = x
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res

        def union(x:int, y:int) -> int:
            p1 = find(x)
            p2 = find(y)

            if p1 == p2:
                return 0
            if rank[p1] < rank[p2]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1
        res = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] ==1:
                    res -= union(i,j)
        return res
        