import pytest

def test_to_run():
    assert 1 == 1

@pytest.mark.skip(reason='misunderstood the API')
def test_to_skip():
    assert 1 == 0
