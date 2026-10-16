import requests, pytest
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
def test_create_booking(booking_client,create_booking):
    booking_id, data = create_booking
    response = booking_client.get_booker(booking_id)
    assert response.status_code==200
    assert data==response.json()
def test_update_booking(booking_client, create_booking):
    booking_id, data = create_booking
    put_response=booking_client.update_booker(booker2, booking_id)
    response = booking_client.get_booker(booking_id)
    assert put_response.status_code==200
    assert response.status_code==200
    assert put_response.json()==response.json()


def test_partial_update_booking(booking_client,create_booking):
    booking_id, data = create_booking
    partial_response=booking_client.partial_update_booker(booking_id)
    response = booking_client.get_booker(booking_id)
    assert partial_response.status_code==200
    assert response.status_code==200
    assert response.json()['firstname']=='Lena'
    assert response.json()['lastname']=='Poleno'
    mode=True
    neizmenyaemye_fieds=['totalprice','depositpaid','bookingdates','additionalneeds']
    for i in neizmenyaemye_fieds:
        if partial_response.json()[i]!=data[i]:
            mode=False
    assert mode
