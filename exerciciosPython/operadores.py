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

# 1) faca um programa que leia um  numero interio e mostre seu sucesor e antecessor


# 2) algoritimo que mostre o dobro, tripo e raiz quadarada de um numero
"""""
n1 = int(input("Digite um valor: "))
d = n1 * 2
t = n1 * 3
raiz = n1**(1/2)
print("O drobro de {} é {} o triplo {} e a raiz é {:.2f} ".format(n1, d, t, raiz))
"""""

#3) ler duas notas e calcule e mostre a media
"""""
nota1 = float(input("nota 1: "))
nota2 = float(input("nota 2: "))
media = (nota1 + nota2) / 2
print("A média das notas é igual a {}".format(media))
"""

#4) ler o valor em metros e converta em cm e mm
"""""
valor1 = float(input("valor 1: "))
centimetros = valor1 * 100
milimetros = valor1 * 1000
print("Centimetros = {:.0f}cm milimetros = {:.0f}mm".format(centimetros, milimetros))
"""

#5) digite um numero e mostre sua tabuada
#6) digite um valor e mostre quantos dolares ela pode comprar
"""""
valor1 = float(input("valor 1: "))
dolar = 5.17
compra = valor1 / dolar
print("voce pode comprar {} dolares".format(dolar))
"""
#7) ler um preço e mostrar o novo valor com 5% de desconto
compra = int(input("valor da compra"))
desconto = 20
total = compra * (desconto/100)
resultado = compra - total
print("Com o desconto ficou {} reais".format(resultado))
#8) ler o salario o mostre com 15% de aumento