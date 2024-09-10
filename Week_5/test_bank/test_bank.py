from bank import value


def test_value():
    assert value("Hello") == 0
    assert value("Hello!") == 0
    assert value("Hello9") == 0


def test_hvalue():
    assert value("h asd!0") == 20


def test_elsevalue():
    assert value("test") == 100
