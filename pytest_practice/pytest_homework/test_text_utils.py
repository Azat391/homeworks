from text_utils import is_palindrome
def test_is_palindrome1():
    assert is_palindrome('топот') is True
def test_is_palindrome2():
    assert is_palindrome('Топот') is True
def test_is_palindrome3():
    assert is_palindrome('python') is False
def test_is_palindrome4():
    assert is_palindrome('А') is True