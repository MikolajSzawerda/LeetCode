import pytest
from app import Solution, ListNode

@pytest.mark.parametrize("i, o", [
(ListNode(1, ListNode(2, ListNode(3))), [1,3,2]),
(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), [1, 4, 2, 3]),
(ListNode(1), [1]),
(ListNode(1, ListNode(2)), [1, 2]),
(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), [1,5,2,4,3])

    ])
def test_case(i, o):
    Solution().reorderList(i)
    assert i is not None
    k = 0
    while i:
        assert i.val == o[k]
        k += 1
        i = i.next
