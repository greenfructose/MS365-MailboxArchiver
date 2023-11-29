import asyncio
from graph import Graph

class Mail():
    def __init__(self, customer_id: str) -> None:
        self.set_customer_id(customer_id)
        self.set_graph()

    def set_customer_id(self, customer_id: str) -> None:
        self._customer_id = customer_id

    def get_customer_id(self) -> str:
        return self._customer_id
    
    def set_graph(self) -> None:
        self._graph = Graph(self.get_customer_id())

    def get_graph(self) -> Graph:
        return self._graph
    
    async def download_all_email(self, user_id: str):
        messages = await self.get_graph().get_client().users.by_user_id(user_id).messages.get()
        for message in messages.value:
            print(message)