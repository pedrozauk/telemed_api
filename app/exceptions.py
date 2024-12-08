
# Exceptions ligadas a operações de banco de dados
class NenhumRegistroRetornado(Exception):
    def __init__(self, *args):
        super().__init__("Nenhum registro encontrado",*args)
