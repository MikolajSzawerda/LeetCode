import pytest
from app import Solution

@pytest.mark.parametrize("i, o", [
([3,4,5,1,2], 1),
([4,5,6,7,0,1,2], 0),
([11,13,15,17], 11),
([12, 13, 1, 8, 9, 10, 11], 1),
    ])
def test_case(i, o):
    assert Solution().findMin(i) == o
