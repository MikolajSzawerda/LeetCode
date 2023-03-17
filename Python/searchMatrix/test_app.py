import pytest
from app import Solution

@pytest.mark.parametrize("i, o", [
    (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3), True),
    (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13), False),
    (([[1,2,4,4,5]], 3), False),
    (([[1], [2], [4], [5]], 3), False),
    (([[3]], 3), True),
    (([[1], [3]], 3), True),
    ])
def test_case(i, o):
    assert Solution().searchMatrix(*i) == o
