import pytest
from app import Solution

@pytest.mark.parametrize("i, o", [
    (["2","1","+","3","*"], 9),
    (["4","13","5","/","+"], 6),
    (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22)
    ])
def test_case(i, o):
    assert Solution().evalRPN(i) == o
