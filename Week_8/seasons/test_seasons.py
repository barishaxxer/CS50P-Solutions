from seasons import Time
import pytest


def test_accuracy():

    assert (
        Time.convert("2023-08-29")
        == "Five hundred twenty-seven thousand, forty minutes"
    )
    assert (
        Time.convert("2022-08-29")
        == "One million, fifty-two thousand, six hundred forty minutes"
    )
    with pytest.raises(SystemExit):
        Time.convert("22/03/05")
