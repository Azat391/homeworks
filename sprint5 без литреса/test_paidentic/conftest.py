import pytest,requests
from paidentic.models import Book_Factory, CustomerFactory, BookingAPI, BookingClient


@pytest.fixture
def create_book():
    factory=Book_Factory()
    return factory.create
@pytest.fixture
def create_customer():
    customer=CustomerFactory()
    return customer.create


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

@pytest.fixture
def booking_api():
    client=BookingAPI('https://restful-booker.herokuapp.com')

    yield client

@pytest.fixture
def create_booking(booking_api):
    response=booking_api.create_booking(booker)
    booking_data = response.json()['booking']
    yield response, booking_data

