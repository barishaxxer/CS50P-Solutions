from numb3rs import validate

def test_longer():
    assert validate("192.168.1.1.1") == False
    assert validate("192.256.5346.254") == False
    assert validate("512.256.5346.254") == False

def test_alpha():
    assert validate("adsasd.sd.sd.asd") == False
    assert validate("297.323.6.28") == False
    assert validate("192.300.1.1") == False
