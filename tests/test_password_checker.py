from lib.password_checker import *

import pytest

def test_8_or_more_char():
    password = PasswordChecker() 
    check = password.check("123456789")
    assert check == True

def test_less_than_8_char():
    password = PasswordChecker() 
    with pytest.raises(Exception) as e:
        password.check("1234567")
    message = str(e.value)
    assert message == "Invalid password, must be 8+ characters."

