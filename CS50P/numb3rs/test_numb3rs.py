from numb3rs import validate

def test_validate():
    assert validate("192.168.1.1") == True
    assert validate("10.20.30.40") == True
    assert validate("300.400.500.600") == False
    assert validate("8.16.32.64") == True
    assert validate("abc.def.ghi.jkl") == False
    assert validate("100.200.300.400") == False
    assert validate("45.67.89.12") == True
    assert validate("255.0.255.128") == True
    assert validate("123.456.789.012") == False
    assert validate("0.0.0.0") == True
