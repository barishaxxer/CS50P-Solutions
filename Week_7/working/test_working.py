from working import convert
import pytest

def test_unittestsarereaallyboring1():
    assert convert("1 AM to 3:00 PM") == "01:00 to 15:00"
    with pytest.raises(ValueError):
        convert("26 AM to 29 PM")


def test_unittestsarereaallyboring2():
    with pytest.raises(ValueError):
        convert("23oldfl")



def test_unittestsarereaallyboring3():
    assert convert("1 AM to 3:00 PM") != "01 to 15"
