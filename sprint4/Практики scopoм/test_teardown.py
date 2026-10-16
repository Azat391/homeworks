import pytest, os
event_log=[]
@pytest.fixture
def event_tracker():
    event_log.append('SETUP')
    yield 'test runnung'
    event_log.append("TEARDOWN")

@pytest.fixture
def temp_note():
    with open('note.txt', 'w') as f:
        f.write('My test note')
    yield 'note.txt'
    os.remove('note.txt')

SHARED_CACHE={}
@pytest.fixture
def clean_cache():
    yield
    SHARED_CACHE.clear()

@pytest.fixture(scope='session')
def test_database():
    yield {
    "status": "connected",
    }
    print("Closing database connection...")

SESSION=[]
@pytest.fixture
def active_session():
    SESSION.append('session')
    yield 
    SESSION.clear()

