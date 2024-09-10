from twttr import shorten


def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("twitter!.") == "twttr!."
    assert shorten("twitter9") == "twttr9"
