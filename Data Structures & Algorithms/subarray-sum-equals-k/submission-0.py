class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0:1}
        curr_sum = 0
        res = 0

        for n in nums:
            curr_sum += n
            diff = curr_sum - k
            res += prefix_sums.get(diff, 0)
            prefix_sums[curr_sum]= 1 + prefix_sums.get(curr_sum, 0)
        return res




        