from abc import ABC, abstractmethod
from xml.sax.handler import property_interning_dict
from models.enum import StatusPedido

class Pedido(ABC):
    @abstractmethod
    def __init__(self, id, cliente:Cliente, valor, status: StatusPedido):
        self._id = id              # atributo protegido
        self._Cliente = cliente    # objeto da classe Cliente
        self._valor = valor
        self._status = status


