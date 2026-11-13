class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        target = sum(nums) % p

        if target == 0:
            return 0 
        #Already divisible by p

        #MAP: prefix_remainder to most_recent_index

        last_seen = { 0: -1}

        curr_rem = 0
        min_len = len(nums)

        for i, num in enumerate(nums):
            curr_rem = (curr_rem + num) % p
            needed_rem = (curr_rem - target + p) %p

            if needed_rem in last_seen:
                min_len = min(min_len, i - last_seen[needed_rem])
            
            last_seen[curr_rem] = i

        return min_len if min_len < len(nums) else -1
        