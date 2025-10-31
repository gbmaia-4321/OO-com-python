import Pedido

class PedidoComida(Pedido):
  def __init__(self, id, cliente:Cliente, valor, status: StatusPedido):
      super().__init__ (id, cliente:Cliente, valor, status: StatusPedido)