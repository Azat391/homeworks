import pytest,requests
# Создание и получение
@pytest.mark.smoke
@pytest.mark.regression
def test_create_pet(pet_client, created_pet):
    pet_id, response_post= created_pet
    response_get= pet_client.get_pet(pet_id)
    assert response_get.status_code==200
    assert response_post.status_code==200
    assert response_get.json()==response_post.json()
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize('status_pet', ['available', 'sold','pending'])
def test_create_pet_with_status(pet_client, pet_factory,status_pet):
    pet_id, response_post= pet_factory(status=status_pet)
    response_get=pet_client.get_pet(pet_id)
    assert response_get.status_code==200
    assert response_get.json()['status']==status_pet
# Поиск несуществующго
@pytest.mark.smoke
@pytest.mark.regression
def test_get_nesuchestvuyuchiy_pet(pet_client, created_pet):
    pet_id, _ = created_pet
    pet_client.delete_pet(pet_id)
    assert pet_client.get_pet(pet_id).status_code==404
# Обновление
@pytest.mark.regression
def test_update_pet(pet_client, pet_factory):
    pet_id_post, response_post= pet_factory()

    assert response_post.status_code==200

    _, data_put=pet_factory(id=pet_id_post, suffix='Azat', status='sold')
    response_put=pet_client.update_pet(data_put.json())
    response_get=pet_client.get_pet(pet_id_post)
    assert response_put.status_code==200
    assert response_get.json()['id']==response_post.json()['id']
    assert response_get.json()['name']==response_put.json()['name']
    assert response_get.json()['status']==response_put.json()['status']
# Обновление статуса
@pytest.mark.regression
@pytest.mark.parametrize('status',['available', 'sold','pending'])
def test_update_status(pet_client, pet_factory,status):
    id, original_data= pet_factory()
    name=original_data.json()['name']
    get_original_pet=pet_client.get_pet(id)
    _, data_put=pet_factory(id=id, suffix=name, status=status)
    changed_pet=pet_client.update_pet(data_put.json())
    get_changed_pet=pet_client.get_pet(id)
    assert changed_pet.status_code==200
    assert get_changed_pet.json()['id']==get_original_pet.json()['id']
    assert get_changed_pet.json()['name']==get_original_pet.json()['name']
    assert get_changed_pet.json()['status']==status
# Поиск по статусу среди всех
@pytest.mark.regression
@pytest.mark.parametrize('status',['available', 'sold','pending'])
def test_find_by_status(pet_client, status):
    response=pet_client.find_by_status(status)
    assert response.status_code==200
    mode=True
    for i in response.json():
        if i['status']!=status:
            mode=False
    assert mode

# Поиск созданного по статусу
@pytest.mark.regression
@pytest.mark.parametrize('status',['available', 'sold','pending'])
def test_find_by_status_created(pet_client, pet_factory,status):
    id, data = pet_factory(status=status)
    response_post=pet_client.create_pet(data.json())
    response_find=pet_client.find_by_status(status)
    assert response_find.status_code==200
    mode=False
    for i in response_find.json():
        if i['id']==id and i['status']==status:
            mode=True
    assert mode
