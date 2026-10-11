class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        count = {n:0 for n in nums}
        perm = []
        res = []
        for n in nums:
            count[n] += 1

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
            for x in count:
                if count[x] > 0:
                    perm.append(x)
                    count[x] -= 1
                    dfs()
                    count[x] += 1
                    perm.pop()
        dfs()
        return res
                

            


        