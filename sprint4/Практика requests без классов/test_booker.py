import requests, pytest
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
base_url='https://restful-booker.herokuapp.com'
class TestBookingsIds:
    def test_status_code(self, get_booking):
        assert get_booking.status_code==200
    def test_type_response(self, get_booking):
        assert type(get_booking.json()) is list
    def test_list(self,get_booking):
        elements=True
        for i in get_booking.json():
            if type(i) is not dict:
                elements=False
        assert elements
    def test_dict(self,get_booking):
        for data in get_booking.json():
            # for j in i:
                assert all('bookingid' in data_objexts for data_objexts in data) #all у гпт подсмотрел
    def test_id(self,get_booking):
        for data in get_booking.json():
            assert all(type(data_objexts) is int for data_objexts in data.values())
            
class TestBooking:
    def test_status_code(self, create_booking):
        assert create_booking.status_code==200
    def test_bookingid(self,create_booking):
        assert type(create_booking.json()['bookingid'])==int
    def test_booking(self,create_booking):
        assert create_booking.json()['booking']==booker
    def test_created_booker(self, get_my_booker):
        assert get_my_booker.status_code==200
    def test_data_booker(self, get_my_booker):
        assert get_my_booker.json()==booker

class TestUpdateBooking:
    def test_status_code(self, update_booking):
        assert update_booking.status_code==200
    def test_booking_name(self,get_my_update_booker):
        assert get_my_update_booker.json()['firstname']=='Alex'
    def test_booking_price(self,get_my_update_booker):
        assert get_my_update_booker.json()['totalprice']==600
    def test_booking_lastname(self,get_my_update_booker):
        assert get_my_update_booker.json()['lastname']=='Laich'
    def test_booking_deposit(self,get_my_update_booker):
        assert get_my_update_booker.json()['depositpaid']==True
    def test_booking_dates(self,get_my_update_booker):
        assert get_my_update_booker.json()['bookingdates']==booker['bookingdates']
    def test_booking_needs(self,get_my_update_booker):
        assert get_my_update_booker.json()['additionalneeds']==booker['additionalneeds']

class TestUpdateBookingNoToken:
    def test_status_code(self, update_booking_without_token):
        assert update_booking_without_token.status_code == 403

class TestDelete:
    def test_delete(self, delete_booking):
        assert delete_booking.status_code==201

@pytest.mark.parametrize(
    "patch_payload, changed_field, expected",
    [
        ({'firstname': 'Maria'}, 'firstname', 'Maria'),
        ({'totalprice': 777}, 'totalprice', 777),
        ({'depositpaid': False}, 'depositpaid', False),
    ],
)
def test_param(patch_payload, changed_field,create_booking, get_token, expected):
    created=create_booking.json()
    booking_id=created['bookingid']
    requests.get(f'{base_url}/booking/{booking_id}', timeout=10,
    headers = {'Content-Type': 'application/json'}).json()
    response_patch=requests.patch(f'{base_url}/booking/{booking_id}',
    json=patch_payload,
    cookies={'token': get_token},
    headers={'Accept': 'application/json'},
    timeout=10)
    patched=(requests.get(f'{base_url}/booking/{booking_id}', timeout=10,
    headers = {'Content-Type': 'application/json'})).json()
    assert patched[changed_field]==expected
    assert response_patch.status_code == 200
    assert patched==response_patch.json()
    response_delete=requests.delete(f'{base_url}/booking/{booking_id}',
    cookies={'token': get_token},
    headers={'Accept': 'application/json'},
    timeout=10)
    assert response_delete.status_code==201
