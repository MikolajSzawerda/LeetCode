import pytest
from app import MinStack

def test_case1():
    s = MinStack()
    s.push(1)
    assert s.top() == 1
    assert s.getMin() == 1
    s.pop()

def test_case2():
    s = MinStack()
    for n in [9, 8, 7, 6, 5]:
        s.push(n)
        assert s.getMin() == n
    for n in [10, 11, 12, 13, 14]:
        s.push(n)
        assert s.getMin() == 5
    for _ in range(5):
        s.pop()
        assert s.getMin() == 5
    for i in range(4):
        s.pop()
        assert s.getMin() == 6+i

def test_case3():
    s = MinStack()
    for n in [1] * 10:
        s.push(n)
    assert s.getMin() == 1
    s.push(-1)
    assert s.getMin() == -1
    s.pop()
    for n in range(10):
        assert s.getMin() == 1
        s.pop()
