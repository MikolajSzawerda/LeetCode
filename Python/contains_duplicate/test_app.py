import pytest
from app import containsDuplicate

@pytest.mark.parametrize(
        "i, o", [
        ([1, 2, 3, 4], False),
        ([1, 2, 3, 1], True),
        ([1,1,1,3,3,4,3,2,4,2], True)
    ]
)
def test_case(i, o):
    assert containsDuplicate(i) == o

