from typing import *

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 < n2 : return self.findMedianSortedArrays(nums2, nums1)
        l,r = 0, n2*2
        while l <= r:
            m2 = (l+r)//2
            m1 = n1+n2-m2
            l1 = float("-inf") if m1 == 0 else nums1[(m1-1)//2]
            l2 = float("-inf") if m2 == 0 else nums2[(m2-1)//2]
            r1 = float("inf") if m1 == n1*2  else nums1[m1//2]
            r2 = float("inf") if m2 == n2*2 else nums2[m2//2]

            if l1 > r2: l = m2+1
            elif l2 > r1: r = m2-1
            else: return (max(l1, l2)+min(r1, r2))/2
        return -1
