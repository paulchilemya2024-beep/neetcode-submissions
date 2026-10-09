class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = [-1] * len(nums1)
        num1Idx = {n:i for i,n in enumerate(nums1)}
        stack = []

        for n in nums2:
            while stack and n> stack[-1]:
                val = stack.pop()
                idx = num1Idx[val]
                res[idx] = n
            if n in num1Idx:
                stack.append(n)
        return res

        

        