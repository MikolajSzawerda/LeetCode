from typing import *

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = nums[0]
        while l<=r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            p = (l+r)//2
            res = min(res, nums[p])
            if nums[p] <= nums[l]:
                r = p-1
            else:
                l = p+1
        return res
