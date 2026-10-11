class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        #Bottom up dynamic programming
        #base Case
        res = []
        if len(nums) == 0:
            return [[]]
        perms = self.permute(nums[1:])

        for p in perms:
            for i in range(len(p) +1):
                p_copy = p.copy()
                p_copy.insert(i,nums[0])
                res.append(p_copy)
        return res
        