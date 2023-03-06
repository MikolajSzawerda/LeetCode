import pytest
from app import Solution

@pytest.mark.parametrize("i, o", [
([2,1,5,6,2,3], 10),
([2,4], 4)
    ])
def test_case(i, o):
    assert Solution().largestRectangleArea(i) == o
