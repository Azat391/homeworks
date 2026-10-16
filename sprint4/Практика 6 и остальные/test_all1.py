from src.checks import get_supported_formats, find_errors, get_score, get_user_info
def test_supports_jpeg():
    assert get_supported_formats()=='Jpeg'
def test_find_errors():
    assert not find_errors('корректные данные')
def test_score_is_in_valid_range():
    assert get_score()>50 and get_score()<100
def test_user_data():
    assert get_user_info()=={
    "id": 101,
    "name": "Alice",
    "status": "active",
    }
