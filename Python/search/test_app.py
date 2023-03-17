import pytest
from app import Solution

@pytest.mark.parametrize("i, o", [
(([4,5,6,7,0,1,2], 0), 4),
(([4,5,6,7,0,1,2], 3), -1),
(([1], 0), -1),
(([0], 0), 0),
(([2, 1], 1), 1),
    ])
def test_case(i, o):
    assert Solution().search(*i) == o
