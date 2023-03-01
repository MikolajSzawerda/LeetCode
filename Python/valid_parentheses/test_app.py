import pytest
from app import Solution

@pytest.mark.parametrize("i, o", [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("(", False)
    ])
def test_case(i, o):
    assert Solution().isValid(i) == o
