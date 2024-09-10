from Veiculo import Veiculo
from Moto import Moto



#instanciando a classe moto
falcon = Moto("Honda", "Falcon nx4", "abc", 2005, 400)
#Exibir uma informação na tela => 
# vai imprimir o RETORNO DO METODO "__STR__()"

print(falcon.__str__())


cerato = Veiculo("Kia","Cerato","IRL", 2011)

print(cerato.__str__())


# Abaixo estou instanciando um objeto
#   da Classe Veiculo
meuUno = Veiculo("Fiat", "Uno com Escada", "ABC-1234", 2000)
print(meuUno.get_marca())
print(meuUno.calcularTempoUso())
meuUno.__ano = 2010
print(meuUno.calcularTempoUso())


teuFusca = Veiculo("Volks", "Fusca do Itamar", "DEF-", 1995)



#print(meuUno.calcularTempoUso())
#print(teuFusca.calcularTempoUso())

#print("")