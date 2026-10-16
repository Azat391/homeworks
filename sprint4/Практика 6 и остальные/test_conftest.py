import pytest
def test_api_request(auth_token):
    assert auth_token=="SECRET_TOKEN_123"

def test_user_id(current_user):
    assert current_user['user_id']==101
def test_user_role(current_user):
    assert current_user['role']=='editor'



def test_api_uses_db_config(db_config):
    assert db_config["host"] == "localhost"