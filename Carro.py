from Veiculo import Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, placa, ano, n_Portas):
        super().__init__(marca, modelo, placa, ano)
        self.__n_Portas = n_Portas
    
    # Override - sobrescrever o metodo __srt__()
    
    def __str__(self):
        ret = super().__str__()
        return f'''{ret}
    -Num. Portas: {self.__n_Portas}'''
    
    