import requests, pytest
base_url='https://restful-booker.herokuapp.com'
booker={
    'firstname': 'Pal',
    'lastname': 'Laich',
    'totalprice': 69,
    'depositpaid': True,
    'bookingdates': {
        'checkin': '2027-08-10',
        'checkout': '2027-08-15',
    },
    'additionalneeds': 'Движуха',
}
@pytest.fixture(scope='session')
def get_token():
    response=requests.post(f'{base_url}/auth', timeout=10,
    json ={
        'username': 'admin',
        'password': 'password123',
    })
    response.raise_for_status()
    auth_data = response.json()
    token = auth_data.get('token')
    if not token:
        raise RuntimeError('API не вернул токен')
    return token

@pytest.fixture
def get_booking():
    response=requests.get(f'{base_url}/booking', timeout=10)
    response.raise_for_status()
    return response


@pytest.fixture
def create_booking():
    response=requests.post(f'{base_url}/booking', timeout=10,
    json = booker,
    headers = {'Content-Type': 'application/json'})
    response.raise_for_status()
    return response
@pytest.fixture
def get_my_booker(create_booking, get_token):
    created=create_booking.json()
    booking_id=created['bookingid']
    response=requests.get(f'{base_url}/booking/{booking_id}', timeout=10,
    headers = {'Content-Type': 'application/json'})
    response.raise_for_status()
    yield response
    # requests.delete(f'{base_url}/booking/{booking_id}',
    # cookies={'token': get_token},
    # headers={'Accept': 'application/json'},
    # timeout=10)
    
@pytest.fixture
def update_booking(get_token,create_booking):
    created=create_booking.json()
    booking_id=created['bookingid']
    response=requests.patch(f'{base_url}/booking/{booking_id}',
    json= {
    'firstname': 'Alex',
    'totalprice': 600,
},
    cookies={'token': get_token},
    headers={'Accept': 'application/json'},
    timeout=10)
    response.raise_for_status()
    yield response

@pytest.fixture
def get_my_update_booker(update_booking, create_booking):
    created=create_booking.json()
    booking_id=created['bookingid']
    response=requests.get(f'{base_url}/booking/{booking_id}', timeout=10,
    headers = {'Content-Type': 'application/json'})
    response.raise_for_status()
    yield response

@pytest.fixture
def update_booking_without_token(create_booking):
    created=create_booking.json()
    booking_id=created['bookingid']
    response=requests.patch(f'{base_url}/booking/{booking_id}',
    json= {
    'firstname': 'None',
    'totalprice': 600,
},
   
    headers={'Accept': 'application/json'},
    timeout=10)

    yield response

@pytest.fixture
def delete_booking(get_token, create_booking):
    created=create_booking.json()
    booking_id=created['bookingid']
    response=requests.delete(f'{base_url}/booking/{booking_id}',
    cookies={'token': get_token},
    headers={'Accept': 'application/json'},
    timeout=10)
    return response