import pytest
from app import Solution

@pytest.mark.parametrize("i,o, k", [
    ([1,3,-1,-3,5,3,6,7], [3,3,5,5,6,7], 3),
    ([1], [1], 1)
    ])
def test_cases(i, o, k):
    assert Solution().maxSlidingWindow(i, k) == o
