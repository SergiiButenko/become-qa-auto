import pytest


def test_except_failed():
    s = 1/0
    assert s is True


def test_except_passes():
    with pytest.raises(ZeroDivisionError):
        s = 1/0
