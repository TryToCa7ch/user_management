import requests

from config import PORTAINER_API_HOST, PORTAINER_API_KEY


class PortainerHelper():
    def __init__(self):
        self.host = PORTAINER_API_HOST
        self.headers = {f"X-Api-Key: {PORTAINER_API_KEY}"}

    def get_users(self):
        url = f'{self.host}/api/users'
        req = requests.get(url, headers=self.headers)
        return req.json()

    def get_user_by_id(self, id: int):
        url = f'{self.host}/api/users/{id}'
        req = requests.get(url, headers=self.headers)
        return req.json()

    def get_roles(self):
        url = f'{self.host}/api/roles'
        req = requests.get(url, headers=self.headers)
        roles = []
        for role in req.json():
            roles += [{"ID": role["Id"]}, {"Name": role["Name"]}]
        return roles

    def add_user(self, username: str, password: str, role: int = 2):
        url = f'{self.host}/api/users'
        body = {"username": username, "password": password, "role": role}
        response = requests.post(url, json=body, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def del_user(self, id: int):
        url = f'{self.host}/api/users/{id}'
        req = requests.delete(url, headers=self.headers)
        return req.status_code

    def update_user(self, id: int, username: str, password: str, role: int):
        url = f'{self.host}/api/users'
        body = {"username": username, "password": password, "role": role}
        response = requests.put(url, json=body, headers=self.headers)
        response.raise_for_status()
        return response.json()
