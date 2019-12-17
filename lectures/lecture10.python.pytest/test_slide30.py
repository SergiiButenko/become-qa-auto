import pytest

def test_succ():
    assert 1 == 1

@pytest.mark.xfail(reason='misunderstood the API')
def test_fail():
    assert 1 == 0
