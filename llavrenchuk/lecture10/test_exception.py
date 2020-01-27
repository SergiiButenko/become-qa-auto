import pytest

@pytest.mark.smoke
def test_except_passes():
        with pytest.raises(ZeroDivisionError):
            s=1/0


     


