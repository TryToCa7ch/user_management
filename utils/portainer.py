import requests

class PortainerHelper():
    def __init__(self):
        self.host = 'http://localhost:9000'
        # self.token = self.get_creds(f'{self.host}/api/auth', 'admin', 'asd1asd2')
        self.headers = {"X-Api-Key": "ptr_VxDh3ET4HmtNa+1OHTqC6Adst3lhmQtFZSRmektWbHI="}

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
        return req.json()

    def del_user(self, id: int):
        url = f'{self.host}/api/users/{id}'
        req = requests.delete(url, headers = self.headers)
        return req.status_code

p = PortainerHelper()
# print(p.add_user("test","test", 2))
print(p.del_user(5))
# print(p.get_users())