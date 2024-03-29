import pytest
from app import Solution
from math import isclose

@pytest.mark.parametrize("i, o", [
(([1,3], [2]), 2.0),
(([1,2], [3,4]), 2.5),
(([-98, -96, -95, -93, -90, -86, -85, -84, -82, -80, -78, -77, -77, -76, -75, -73, -72, -71, -71, -67, -67, -66, -66, -60, -50, -50, -49, -46, -42, -40, -40, -35, -35, -32, -29, -27, -24, -23, -23, -13, -10, -10, -10, -10, -6, 1, 2, 4, 6, 7, 8, 9, 9, 11, 12, 15, 16, 17, 19, 20, 21, 29, 30, 32, 32, 37, 37, 38, 40, 43, 46, 48, 51, 54, 55, 55, 59, 59, 60, 61, 61, 62, 62, 63, 69, 72, 73, 73, 74, 78, 80, 83, 83, 85, 88, 90, 91, 91, 96, 99], [-100, -99, -95, -92, -87, -82, -77, -67, -67, -66, -66, -65, -58, -52, -52, -41, -31, -30, -23, -20, -12, -11, -11, -8, -6, 1, 7, 10, 19, 20, 21, 22, 22, 25, 25, 29, 31, 33, 33, 35, 40, 44, 44, 49, 50, 51, 52, 52, 55, 57, 61, 62, 62, 64, 66, 69, 74, 76, 79, 91]), 9.5),
(([], [1]), 1),
(([1,3], [2,7]), 2.5),
])
def test_case(i, o):
    assert Solution().findMedianSortedArrays(*i) == o


