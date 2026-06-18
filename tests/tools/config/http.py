from pydantic import BaseModel, IPvAnyAddress, HttpUrl


class HTTPClientTestConfig(BaseModel):
    """
    Конфигурация HTTP-клиента в тестовом окружении.

    Используется всеми HTTP-клиентами тестового слоя.
    """

    url: HttpUrl
    timeout: float = 120.0


class HTTPServerTestConfig(BaseModel):
    port: int
    address: IPvAnyAddress