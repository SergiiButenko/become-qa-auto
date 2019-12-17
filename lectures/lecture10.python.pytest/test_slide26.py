import pytest

@pytest.mark.regression
@pytest.mark.smoke
def test_smoke_reg():
    with pytest.raises(ZeroDivisionError):
        s = 1/0
