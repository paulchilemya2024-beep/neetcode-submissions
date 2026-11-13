class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:

        prefix_cnt = defaultdict(int)
        prefix_cnt[0] = 1
        res = 0
        count = 0

        for n in nums:
            count += n
            remainder = count % k
            res += prefix_cnt[remainder]
            prefix_cnt[remainder] += 1
        return res
            
        