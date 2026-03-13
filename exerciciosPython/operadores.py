"""""
n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))
resultado = n1 + n2
print('A soma entre {} e {} é igual a {}'.format(n1, n2, resultado))
"""
#-----------------------------

""""
n1 = int(input("digite uma valor: "))
n2 = int(input("digite outro numero: "))
soma = n1 + n2
divisao = n1/n2
di = n1 // n2
mult = n1 * n2
print("A soma é {} o produto e {} e divisão e {:.2f}".format(soma, mult, divisao))
"""
#-------------------------------
"""""
# 1) ler um  numero interio e mostre seu sucesor e antecessor
n = int(input("numero: "))
a = n - 1
s= n + 1
print(f"Analisando o numero {n} seu antecessor é {a} e o sucessor {s}")
"""

# 2) algoritimo que mostre o dobro, tripo e raiz quadarada de um numero
"""""
n1 = int(input("Digite um valor: "))
d = n1 * 2
t = n1 * 3
raiz = n1**(1/2)
print(f"O drobro de {n1} é {d} o triplo {t} e a raiz é {:.2f} ")
"""""

#3) ler duas notas e calcule e mostre a media
"""""
nota1 = float(input("nota 1: "))
nota2 = float(input("nota 2: "))
media = (nota1 + nota2) / 2
print(f"A média das notas é igual a {media}")
"""

#4) ler o valor em metros e converta em cm e mm
"""""
medida = float(input("valor 1: "))
centimetros = medida * 100
milimetros = medida * 1000
print("Centimetros = {:.0f}cm\n milimetros = {:.0f}mm".format(centimetros, milimetros))

#5) digite um numero e mostre sua tabuada

#6) digite um valor e mostre quantos dolares ela pode comprar
valor1 = float(input("valor 1: "))
dolar = 5.17
compra = valor1 / dolar
print("voce pode comprar {} dolares".format(dolar))


#7) LER UM PREÇO E MOSTRAR COM 5% DE DESCONTO
compra = float(input("valor da compra: "))
desconto = 5
total = compra - (compra*desconto/100)
print(f"Com o desconto de {desconto}% ficou {total:.2f} reais")

#8) LER O SALARIO E MOSTRAR COM 15% DE AUMENTO
salario = int(input("digite seu salario: "))
aumento = 15
reajuste = salario + (salario * aumento/100)
print(f"Com o reajuste de 15% o salário ficou {total:.2f} reais")


#9) CONVERSOR DE G° PARA FAHRENHEIT
graus = float(input("valor em graus: "))
f = 9 * graus/5 + 32
print(f"A converção de {graus} para Fahrenheit é de {f}F")
"""

#aluguel de carro calculando o preço a pagar, 
#sabendo que o carro custa 60 por dia e 0.15 por km rodado
dias = int(input("quantos dias de aluguel: "))
kms = float(input("quantos km: "))
pagar = (dias * 60) + (kms *0.15)
print(f"O valor toltal a se pagar é de {pagar:.2f} reais")