from um import count


def test_um1():
    assert count("um") == 1


def test_um2():
    assert count("um?") == 1


def test_um3():
    assert count("yummy") == 0
    assert count(" um ") == 1
    assert count("UM") == 1
