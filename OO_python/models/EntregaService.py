from abc import ABC, abstractclassmethod

# define interface usando ABC
class EntregaService(ABC):
  @abstractmethod
  def getTempoEstimado():
    pass

  @abstractmethod
  def isPedidoUrgente():
    pass
