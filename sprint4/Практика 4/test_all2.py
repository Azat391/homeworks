import pytest
from src.checks2 import division_on_zero, get_user_by_id, set_new_password

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        division_on_zero(5,0)

def test_user_not_found():
    with pytest.raises(KeyError):
        get_user_by_id(999)

def test_user_found_successfully():
    assert get_user_by_id(1)

def test_password_too_short_message():
    with pytest.raises(ValueError) as excinfo:
        set_new_password('SAS')
    assert 'Пароль слишком короткий' in str(excinfo.value)

def test_pop_from_empty_list():
    list=[]
    with pytest.raises(IndexError):
        list.pop()

