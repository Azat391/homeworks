import pytest,requests

class PetClient:
    def __init__(self,base_url,timeout):
        self.base_url=base_url
        self.timeout=timeout
        self.session=requests.Session()
        self.session.headers.update({'Accept':'application/json'})
    def create_pet(self,payload):
        response=self.session.post(f'{self.base_url}/pet', timeout=self.timeout,
        json=payload)
        return response
    def get_pet(self,pet_id):
        response = self.session.get(f'{self.base_url}/pet/{pet_id}', timeout=self.timeout)
        return response
    def update_pet(self,payload):
        response= self.session.put(f'{self.base_url}/pet',timeout=self.timeout,
        json=payload)
        return response
    def find_by_status(self,status):
        response= self.session.get(f'{self.base_url}/pet/findByStatus',timeout=self.timeout,
        params={'status':f'{status}'})
        return response
    def delete_pet(self,pet_id):
        response=self.session.delete(f'{self.base_url}/pet/{pet_id}', timeout=self.timeout)
        return response
    def close(self):
        self.session.close()