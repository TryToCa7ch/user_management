import routeros_api

class Mikrotik_helper:
    def __init__(self):
        self.host = 'localhost'
        self.port = 18728
        self.username = 'admin'
        self.password = '123'
        self.connection = routeros_api.RouterOsApiPool(host=self.host, port=self.port, username=self.username, password=self.password,  plaintext_login=True)

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

    def add_secret(self, username: str, password: str, service:str ='l2tp', profile: str ='default') -> list:
        api = self.connection.get_api()
        api.get_resource('/ppp/secret').add(name=username, password=password, service=service, profile=profile)
        return self.get_secret_by_name(username)
        

