import pytest
import sys
@pytest.mark.smoke
def test_check_status():
    assert True

@pytest.mark.skip(reason='Feature not ready')
def test_unimplemented_feature():
    assert False  # Этот assert никогда не должен выполниться

@pytest.mark.skipif(
    sys.version_info < (3, 10),
    reason='Requires Python 3.10+'
)
def test_python310_feature():
    # Тест использует match-case, который появился в Python 3.10
    value = 1

    match value:
        case 1:
            assert True

@pytest.mark.xfail(reason='Known bug in calculation module, see TICKET-42')
def test_known_bug():
    # 0.1 + 0.2 в Python не равно в точности 0.3
    assert 0.1 + 0.2 == 0.3

@pytest.mark.smoke
@pytest.mark.api
def test_user_authentication():
    assert True