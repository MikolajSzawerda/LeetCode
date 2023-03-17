from typing import *

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)*len(matrix[0])-1
        m = len(matrix[0])
        n = len(matrix)
        while l<=r:
            p = (l+r)//2
            i = p % m
            j = (p-i) // m
            if matrix[j][i] > target:
                r = p-1
            elif matrix[j][i] < target:
                l = p+1
            else:
                return True
        return False

