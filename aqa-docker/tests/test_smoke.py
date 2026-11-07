import pytest


@pytest.mark.smoke
def test_python_test_environment_starts():
    assert 2 + 2 == 4


    
@pytest.mark.smoke
def test_cache_demo():
    assert True
