import pytest
from app import Solution

@pytest.mark.parametrize("i, o", [
(([3,6,7,11], 8), 4),
(([30,11,23,4,20], 5), 30),
(([3], 9), 1),
(([312884470], 968709470), 1),
])
def test_case(i, o):
    assert Solution().minEatingSpeed(*i) == o
