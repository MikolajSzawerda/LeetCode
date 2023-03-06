from typing import *

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                res = max(res, stack[-1][0]*(i-stack[-1][1]))
                start = stack[-1][1]
                stack.pop()
            stack.append((h, i))
        for h,i in stack:
            res = max(res, h*(len(heights)-i))
        return res

