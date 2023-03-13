import requests
from requests.exceptions import RequestException

class PortainerHelper():
    def __init__(self):
        self.host = 'http://localhost:9000'
        # self.token = self.get_creds(f'{self.host}/api/auth', 'admin', 'asd1asd2')
        self.headers = {"X-Api-Key": "ptr_B0B35M1o8fAZaW0yE3tGELRXWv40g6W9FM80GPKy7AI="}

    # def get_creds(self, url, user, password):
    #     self.url = url
    #     body = {"username": user, "password": password}
    #     req = requests.post(url, json = body)
    #     return req.json()['jwt']

    def get_users(self):
        url = f'{self.host}/api/users'
        req = requests.get(url, headers = self.headers)
        return req.json()
    
    def get_user_by_id(self, id: int):
        url = f'{self.host}/api/users/{id}'
        req = requests.get(url, headers = self.headers)

    def get_roles(self):
        url = f'{self.host}/api/roles'
        req = requests.get(url, headers = self.headers)
        roles = []
        for role in req.json():
            roles += [{"ID": role["Id"]}, {"Name": role["Name"]}]
        return roles

    def add_user(self, username: str, password: str, role: int = 2 ):
        url = f'{self.host}/api/users'
        body = {"username": username, "password": password, "role": role}
        req = requests.post(url, json = body, headers = self.headers)
        if req.status_code != 200:
            raise Exception(req.json())
        else:
            return req.json()

    def del_user(self, id: int):
        url = f'{self.host}/api/users/{id}'
        req = requests.delete(url, headers = self.headers)
        return req.status_code

    def update_user(self, id: int, username: str, password: str, role: int):
        url = f'{self.host}/api/users'
        body = {"username": username, "password": password, "role": role}
        req = requests.put(url, json = body, headers = self.headers)
        if req.status_code != 200:
            raise RequestException
        else:
            req.json()