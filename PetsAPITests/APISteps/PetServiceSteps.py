import json
import requests

from TestSettings import valid_email


class Pets:

    def __init__(self):
        self.my_token = None
        self.base_url = 'http://34.141.58.52:8000/'

    def get_token(self) -> json:
        data = {"email": 'vadim@mail.com',
                "password": '2281488'}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        status = res.status_code
        print(my_token)
        print(res.json())
        return my_token, status, my_id

    def get_token_with_invalid_creds(self, login, password) -> json:
        data = {"email": login,
                "password": password}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))

        return res.status_code

    def get_list_users(self):
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        amount = res.json

        print(res.json())
        return status, amount

    def add_pet(self, name, pet_type, age):
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": my_id,
                "name": name, "type": pet_type, "age": age, "owner_id": my_id}
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        print(pet_id)
        print(res.json())
        return pet_id, status

    def get_pet(self, pet_id):
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}

        res = requests.get(self.base_url + "pet/" + pet_id, headers=headers)

        data = json.loads(res.content)
        name_pet = data["pet"]["name"]

        return name_pet

    def add_pet_with_invalid_password(self, invalid_password, name, pet_type, age):
        my_token = Pets().get_token_with_invalid_creds(valid_email, invalid_password)
        my_id = Pets().get_token()[2]

        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": my_id,
                "name": name, "type": pet_type, "age": age, "owner_id": my_id}

        return requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers).status_code

    def delete_pet(self, pet_id):
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}

        requests.delete(self.base_url + "pet/" + pet_id, headers=headers)
        status_code = requests.get(self.base_url + "pet/" + pet_id, headers=headers).status_code

        return status_code

    def update_pet_name(self, name, pet_type, age, pet_id):
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": my_id,
                "name": name}
        requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)

        response = requests.get(self.base_url + "pet/" + pet_id, headers=headers)

        response_data = json.loads(response.content)
        name_pet = response_data["pet"]["name"]

        status = response.status_code

        return name_pet, status
