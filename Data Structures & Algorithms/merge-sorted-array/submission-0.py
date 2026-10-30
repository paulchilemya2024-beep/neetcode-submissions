class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # for i in range(n):
        #     nums1[m+i] = nums2[i]
        # nums1.sort()

        p1 = m-1 # Points to the last real element in nums1
        p2 = n-1 # Points to the last real element in nums2
        p = m+n-1 # Point to the very end of nums1 where the largest remaining value will be placed

        while p1>= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1-=1
            else:
                nums1[p] = nums2[p2]
                p2 -=1
            p -= 1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p-= 1
        