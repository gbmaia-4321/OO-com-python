class EntregaPedido(EntregaService):
  def getTempoEstimado(self):
    if isPedidoUrgente == True:
      return print("Tempo medio estimado de 30 minutos")

    else:
      return print("Tempo medio estimado de 50 minutos")
