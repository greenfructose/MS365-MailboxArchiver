from configparser import ConfigParser
from azure.identity.aio import ClientSecretCredential
from msgraph_beta import GraphServiceClient


class Graph():
    def __init__(self, customer_id: str) -> None:
        self.set_customer_id(customer_id)
        self.set_config()
        self.set_credential()
        self.set_scopes()
        self.set_client()

    def set_customer_id(self, customer_id: str) -> None:
        self._customer_id = customer_id

    def get_customer_id(self) -> str:
        return self._customer_id

    def set_config(self) -> None:
        config = ConfigParser()
        config.read('graph.cfg')
        self._config = config[self.get_customer_id()]

    def get_config(self) -> ConfigParser:
        return self._config
    
    def get_tenant_id(self) -> str:
        return self.get_config()['tenant_id']
    
    def get_client_id(self) -> str:
        return self.get_config()['tenant_id']
    
    def get_client_secret(self) -> str:
        return self.get_config()['tenant_id']
    
    def set_credential(self) -> None:
        self._credential = ClientSecretCredential(
            self.get_tenant_id(),
            self.get_client_id(),
            self.get_client_secret()
        )

    def get_credential(self) -> ClientSecretCredential:
        return self._credential
    
    def set_scopes(self) -> None:
        self._scopes = ['https://graph.microsoft.com/.default']

    def get_scopes(self) -> list:
        return self._scopes
    
    def set_client(self) -> None:
        self._client = GraphServiceClient(
            self.get_credential(),
            scopes=self.get_scopes()
        )

    def get_client(self) -> GraphServiceClient:
        return self._client