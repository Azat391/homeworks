import pytest,requests
from clients.pet_clients import PetClient       
from data.pet_factory import create_data
from config import BASE_URL, TIMEOUT
@pytest.fixture
def pet_client():
    api_client= PetClient(BASE_URL,TIMEOUT)
    yield api_client
    api_client.close()
@pytest.fixture
def pet_factory(pet_client):
    pet_ids=[]
    def _pet_clients(id=None, suffix=None, status=None):
        pet_data=create_data(id=id,suffix=suffix, status=status)
        response= pet_client.create_pet(pet_data)
        pet_id=response.json()['id']
        pet_ids.append(pet_id)
        return pet_id, response
    yield _pet_clients
    for i in pet_ids:
        pet_client.delete_pet(i)
@pytest.fixture
def created_pet(pet_client,suffix=None, status=None):
    data=create_data(suffix,status)
    response=pet_client.create_pet(data)
    pet_id=response.json()['id']
    yield pet_id, response
    pet_client.delete_pet(pet_id)


