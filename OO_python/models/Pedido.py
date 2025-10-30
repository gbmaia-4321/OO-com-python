from pedido import Pedido, abstractmethod
from models.enums import StatusPedido

class Pedido(Pedido):

    def __init__(self, id, cliente, valor, status: StatusPedido):
        self._id = id              # atributo protegido
        self._cliente = cliente    # objeto da classe Cliente
        self._valor = valor
        self._status = status