import pytest

@pytest.fixture()
def age_yield():
    print("setup user")
    yield 43
    print("remove user")


def test_age_s_t(age_yield):
    """Use fixture return value in a test."""
    assert age_yield == 43
