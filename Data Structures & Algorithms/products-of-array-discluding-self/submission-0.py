class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix_pro = 1

        for i in range(len(nums)):
            res[i] = prefix_pro
            prefix_pro *= nums[i]
        
        postfix_pro = 1

        for j in range(len(nums)-1,-1,-1):
            res[j] *= postfix_pro
            postfix_pro *= nums[j]
        return res
