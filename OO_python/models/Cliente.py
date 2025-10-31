
class Cliente:
  def __init__(self,id, nome,email, telefone, endereco):
    self._id = id
    self._nome = nome
    self._email = email
    self._telefone = telefone
    self._endereco = endereco

    print(file="Cliente criado com sucesso!")