"""""
tempo = int(input("quantos anos tem seu carro: "))
if tempo <= 3:
    print("seu carro é novo")
else:
    print("seu carro é antigo")

----------------
nome = str(input("Qual o seu nome?: "))
if nome == "Hugo":
    print("Que nome bonito!!")
else:
    print(":)")
print(f"Bom dia, {nome}")
----------------------

n1 = float(input("nota 1: "))
n2 = float(input("nota 2: "))
media = (n1 * n2)/ 2
if media <=5:
    print("repravado")
else:
    print("aprovado")


#DESCOBRIR QUAL NUMERO A MAQUINA "PENSOU"
import random 
numeros = [1,2,3,4,5]
numeroescolhido = random.choice(numeros)
escolha = int(input("escolha um numero: "))
if escolha == numeroescolhido:
    print("vc acertou o numero")
else:
    print("vc errou o numero")
print(f"O numero era {numeroescolhido}")

#LER A VELOCIDADE DE UM CARRO. SE ULTRAPASSAR 80KM/H MOSTRAR QUE FOI MULTADO
#E A MULTA VAI CUSTAR 7,00 POR CADA KM aCIMA DO LIMITE

velocidade = int(input("Qual foi a velocidade do veiculo? "))
multa = velocidade 
if velocidade > 80:
    print("Vc foi multado")

#NUMERO PAR OU IMPAR
n1 = int(input("Numero "))
if n1 % 2 == 0 :
    print("o numero é par")
elif n1 % 2 == 1:
    print("O numero é impar")

#PERGUNTAR A DISTANCIA EM KMS, CALCULAR O PREÇO DA PASSAGEM COBRANDO 0,50 POR KM ATE 200KM
# E 0,45 PARA VIAGENS MAIS LONGAS
viagem = int(input("Quantos Kms de viagem "))
if viagem <= 200:
    print(f"Vc devera pagar {viagem * 0.50}")
else:
    print(f"A viagem custou {viagem * 0.45}")
"""

#SABER SE UM ANO É BISSEXTO
ano = int(input("Digite um ano"))
divisor = 4