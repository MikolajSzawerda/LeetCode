import pytest
from app import Solution

@pytest.mark.parametrize("i, o", [
    ((12, [10,8,0,5,3],[2,4,1,1,3]), 3),
    ((10, [3], [3]), 1),
    ((100, [0,2,4],[4,2,1]), 1)
    ])
def test_case(i, o):
    assert Solution().carFleet(*i) == o
