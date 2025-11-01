from models import Pedido, Cliente, StatusPedido

class PedidoComida(Pedido):

  def __init__(self, id, cliente:Cliente, distancia, valor, status: StatusPedido):
      super().__init__ (id, cliente, distancia, valor, status)


    # implementando metodos herdados
  def calcularTaxa(self):
    if self._valor > 20.00:
      return 0.0 #taxa gratuita

    else:
      return 5.0

  def getDetalhes(self):
    taxa = self.calcularTaxa()
    valor_total = self._valor + taxa

    return{
      'id': self._id,
      'cliente': str(self._cliente),
      'valor_produtos': self._valor,
      'taxa_entrega': taxa,
      'valor_total': valor_total,
      'status': self._status,
      'tem_entrega_gratis': taxa == 0.0
    }
