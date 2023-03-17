import pytest
from app import Solution, ListNode

@pytest.mark.parametrize("i, o", [
((ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2), [1,2,3,5]),
((ListNode(1), 1), []),
((ListNode(1, ListNode(2)), 1), [1]),
((ListNode(1, ListNode(2, ListNode(3))), 3), [2, 3]),
    ])
def test_case(i, o):
    h = Solution().removeNthFromEnd(*i)
    i = 0
    for num in o:
        assert h.val == num
        h = h.next
