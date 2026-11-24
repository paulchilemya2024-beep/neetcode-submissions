class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = list(range(n+1))
        rank = [1] * (n+1)

        def find(x:int) -> int:
            res = x
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]     
            return res
        
        def union(x:int, y:int) -> bool:
            p1, p2 = find(x), find(y)

            if p1 == p2:
                return False
            
            if rank[p1] < rank[p2]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return True
        
        for i, r in edges:
            if not union(i,r):
                return [i,r]
            

        


        