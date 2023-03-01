from typing import *

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while s and t > temperatures[s[-1]]:
                res[s[-1]] = i - s[-1]
                s.pop()
            s.append(i)
        return res
