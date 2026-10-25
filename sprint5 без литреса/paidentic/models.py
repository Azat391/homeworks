from datetime import date
from pydantic import BaseModel, model_validator, Field
import pytest, requests
class Book(BaseModel):
    title: str 
    author: str
    pages: int = Field( gt=0, strict=True)
    descriptions: str | None = None
class Book_Factory:
    def create(self,**overrides):
        return Book(**overrides)

class Adress(BaseModel):
    city: str
    street: str
class Customer(BaseModel):
    name: str
    address: Adress
class CustomerFactory:
    def create(self,**overrides):
        return Customer(**overrides)

class BookingDates(BaseModel):
    checkin: date
    checkout: date
    @model_validator(mode='after')
    def check_order(self):
        if self.checkout <= self.checkin:
            raise ValueError('Дата выезда должна быть позже даты заезда')
        return self


base_url='https://restful-booker.herokuapp.com'

class BookingAPI:
    def __init__(self,base_url):
        self.session=requests.Session()
        self.base_url=base_url
        self.timeout=60
        self.session.headers.update({
            'Accept': 'application/json',
        })
    def create_booking(self,booker):
        response=self.session.post(f'{self.base_url}/booking', timeout=self.timeout,
        json = booker)
        return response    


class BookingClient(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str
class CreatedBooking(BaseModel):
    id: int
    booking: BookingClient