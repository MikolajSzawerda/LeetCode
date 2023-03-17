import pytest
from app import TimeMap

def test_case1():
    tm = TimeMap()
    tm.set("f", "b", 1)
    assert tm.get("f", 1) == "b"
    tm.set("f", "c", 2)
    tm.set("f", "d", 5)
    tm.set("f", "e", 6)
    assert tm.get("f", 7) == "e"

def test_case2():
    tm = TimeMap()
    tm.set("f", "a", 1)
    tm.set("f", "b", 1)
    tm.set("f", "d", 1)
    tm.set("f", "e", 1)
    tm.set("f", "f", 1)
    assert tm.get("f", 1) == "f"

def test_case3():
    tm = TimeMap()
    tm.set("f", "b", 10)
    assert tm.get("f", 2) == ""

def test_case4():
    tm = TimeMap()
    tm.set("love", "high", 10)
    tm.set("love", "low", 20)
    assert tm.get("love", 5) == ""
    assert tm.get("love", 10) == "high"
    assert tm.get("love", 15) == "high"
    assert tm.get("love", 20) == "low"
    assert tm.get("love", 25) == "low"
