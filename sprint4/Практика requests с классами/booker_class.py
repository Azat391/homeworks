import pytest, requests
base_url='https://restful-booker.herokuapp.com'

class BookingClient:
    def __init__(self,base_url):
        self.session=requests.Session()
        self.base_url=base_url
        self.timeout=10
        self.session.headers.update({
            'Accept': 'application/json',
        })
    def authentiticate(self):
        response=self.session.post(f'{self.base_url}/auth', timeout=self.timeout,
        json ={
            'username': 'admin',
            'password': 'password123',
        })
        response.raise_for_status()
        token = response.json().get('token')
        if not token:
            raise RuntimeError('API не вернул токен')
        self.session.cookies.set('token', token)
    def create_booking(self,booker):
        response=self.session.post(f'{self.base_url}/booking', timeout=self.timeout,
        json = booker)
        response.raise_for_status()
        booking_id=response.json()['bookingid']
        return response
    def get_booker(self, booking_id):
        response = self.session.get(f'{self.base_url}/booking/{booking_id}', timeout=self.timeout)
        response.raise_for_status()
        return response
    def update_booker(self,booker2,booking_id):
        response= self.session.put(f'{self.base_url}/booking/{booking_id}', 
        timeout=self.timeout, json = booker2,
        )
        response.raise_for_status()
        return response

    def partial_update_booker(self,booking_id):
        response= self.session.patch(f'{self.base_url}/booking/{booking_id}', timeout=self.timeout, 
        json = {'firstname': 'Lena', 'lastname': 'Poleno'})
        response.raise_for_status()
        return response
    
    def delete_booker(self,booking_id):
        response=self.session.delete(f'{self.base_url}/booking/{booking_id}',
        timeout=self.timeout)
        return response
    def close(self):
        self.session.close()

