from plates import is_valid

def test_isvalid1():
    assert is_valid("CS50") == True
def test_isvalid2():
    assert is_valid("123456") == False
def test_isvalid3():
    assert is_valid("CS50P2") == False

def test_isvalid4():
    assert is_valid("012Abu") == False
    assert is_valid("AA012") == False
    assert is_valid("ABC!!?") == False
    assert is_valid("23asdk") == False
    assert is_valid("NRVOUS") == True
    assert is_valid("AAAANRVOSUA") == False





