import routeros_api

from config import MIKROTIK_API_HOST, MIKROTIK_API_PORT, MIKROTIK_USER, MIKROTIK_PASSWORD


class MikrotikHelper:
    def __init__(self):
        self.host = MIKROTIK_API_HOST
        self.port = MIKROTIK_API_PORT
        self.username = MIKROTIK_USER
        self.password = MIKROTIK_PASSWORD
        self.connection = routeros_api.RouterOsApiPool(host=self.host,
                                                       port=self.port,
                                                       username=self.username,
                                                       password=self.password,
                                                       plaintext_login=True)

    def get_secrets(self) -> list:
        api = self.connection.get_api()
        get = api.get_resource('/ppp/secret').get()
        return list(get)

    def get_secret_by_name(self, username: str) -> list:
        api = self.connection.get_api()
        get = api.get_resource('/ppp/secret').get(name=username)
        if get:
            return list(get)
        else:
            raise ValueError("There's no secret record ")

    def add_secret(self, username: str, password: str, service: str = 'l2tp', profile: str = 'default') -> list:
        api = self.connection.get_api()
        api.get_resource('/ppp/secret').add(name=username, password=password, service=service, profile=profile)
        return self.get_secret_by_name(username)
