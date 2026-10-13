class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def dfs(total, i, curr):
            if total == target:
                res.append(curr[:])
                return
            if total> target or i >= len(candidates):
                return 
            
            #choose i
            curr.append(candidates[i])
            dfs(total + candidates[i],i+1,curr)

            #do not choose i
            curr.pop()
            while i+1< len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(total,i+1,curr)
        dfs(0,0,[])
        return res
                    