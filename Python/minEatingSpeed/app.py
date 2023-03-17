from typing import *
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l<=r:
            p = (l+r)//2
            s = sum(ceil(pi/p) for pi in piles)
            if s <= h:
                res = min(p, res)
                r = p-1
            else:
                l = p+1
        return res
