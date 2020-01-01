import pytest

@pytest.fixture()
def age():
    return 42

def test_age(age):
    """Use fixture return value in a test."""
    assert age == 42