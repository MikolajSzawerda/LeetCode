import pytest
from app import Solution

@pytest.mark.parametrize("i, o", [
    (3, set(["((()))","(()())","(())()","()(())","()()()"])),
    (1, set(["()"])),
    (2, set(["()()", "(())"]))
    ])
def test_case(i, o):
    assert set(Solution().generateParenthesis(i)) == o
