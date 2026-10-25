import pytest,requests
from pydantic import ValidationError
from paidentic.models import CreatedBooking
@pytest.mark.parametrize('pages', [0,-10,'200'])
def test_unvalid_pages(create_book, pages):
    with pytest.raises(ValidationError):
        create_book(pages=pages)
@pytest.mark.parametrize('data', [{
    "title": "Python Basics", 
    "author": "Alex",
    "pages": 200}, 
    {
    "title": "Python Basics",
    "author": "Alex",
    "pages": 200, 'descriptions': 'Zalupa'},
    {
    "title": "Python Basics",
    "author": "Alex",
    "pages": 200, 'descriptions': None}])
def test_neobezatelnye_field(create_book, data):
    book=create_book(**data)
    if 'descriptions' in data and data['descriptions'] is not None:
        assert book.descriptions==data['descriptions']
    else:
        assert book.descriptions is None
def test_customer(create_customer):
    data={
    "name": "Anna",
    "address": {
        "city": "Kazan",
        "street": "Central",
    },
}
    customer=create_customer(**data)
    assert customer.address.city=='Kazan'
def test_booking_dates(create_booking, booking_api):
    response,booking_data=create_booking
    booking=CreatedBooking.model_validate(response.json())

    assert booking.firstname==booking_data['firstname']
    assert booking.totalprice==booking_data['totalprice']
