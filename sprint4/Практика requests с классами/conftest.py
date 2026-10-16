import pytest
from src.booker_class import BookingClient
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
booker2={
        'firstname': 'Laim',
        'lastname': 'Laimych',
        'totalprice': 140,
        'depositpaid': False,
        'bookingdates': {
            'checkin': '2027-08-10',
            'checkout': '2027-08-15',
        },
        'additionalneeds': 'Движуха',
        }
@pytest.fixture
def booking_client():
    client=BookingClient('https://restful-booker.herokuapp.com')
    client.authentiticate()
    yield client
    client.close()
@pytest.fixture
def create_booking(booking_client):
    response=booking_client.create_booking(booker)
    booking_id = response.json()['bookingid']
    booking_data = response.json()['booking']
    yield booking_id, booking_data
    booking_client.delete_booker(booking_id)