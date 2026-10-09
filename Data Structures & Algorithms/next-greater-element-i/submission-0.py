class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = [-1] * len(nums1)
        num1Idx = {n:i for i,n in enumerate(nums1)}

        for i in range(len(nums2)):
            if nums2[i] not in num1Idx:
                continue
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = num1Idx[nums2[i]]
                    res[idx] = nums2[j]
                    break
        return res