from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            p = (l+r)//2
            if nums[p] == target:
                return p
            if nums[l] <= nums[p]:
                if nums[p] < target or target < nums[l]:
                    l = p +1
                else:
                    r = p-1
            else:
                if target < nums[p] or target > nums[r]:
                    r = p - 1
                else:
                    l = p +1
        return -1
