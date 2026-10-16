import pytest

def square(n):
    return n**2
@pytest.mark.parametrize(
    'n', [2,5,-3]
)
def test_square(n):
    assert square(n)==n**2

def subtract(a,b):
    return a-b

@pytest.mark.parametrize(
    'a,b,expected',[(10,5,5), (5,10,-5), (0,0,0)]
)
def test_subtract(a,b,expected):
    assert subtract(a,b)==expected

def is_palindrome(word):
    return word.lower() == word.lower()[::-1]
# ИСПРАВЬТЕ ДАННЫЕ В СПИСКЕ НИЖЕ
@pytest.mark.parametrize(
    "word, expected",
    [
        ("level", True),
        ("stepik",False),  # ОШИБКА ЗДЕСЬ, СПАСИБО
        ("Noon", True),
    ],
)
def test_is_palindrome(word, expected):
    assert is_palindrome(word) == expected

def get_size(object):
    return len(object)
@pytest.mark.regression
@pytest.mark.parametrize('object', ['pyrest', [1,2,3,4], ()]
)
def test_get_size(object):
    assert get_size(object)==len(object)


def subtract(a,b):
    return a-b
@pytest.mark.smoke
@pytest.mark.parametrize(
    'a,b,expected',[pytest.param(10,5,5,id='Positive'), pytest.param(5,10,-5,id='Negative'), pytest.param(0,0,0, id='Zero')]
)
def test_subtract2(a,b,expected):
    assert subtract(a,b)==expected