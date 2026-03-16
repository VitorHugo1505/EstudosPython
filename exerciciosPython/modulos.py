import math
"""""
num = int(input("gigite um numero: "))
raiz = math.sqrt(num)
print(f"a raiz de {num} é igual a {math.ceil(raiz)}")

#1)--------
n1 = float(input("digite um numero"))
print(f"A porcao inteira do numero {n1} é de {math.trunc(n1)}")


#2) calcular hipotenusa
co = float(input("cateto oposto: "))
ca = float(input("cateto adjacente: "))
hi = math.hypot(co, ca)
print(f"A hipotenusa é igual a {hi:.2f}")


#seno cosseno e tanjente
num = int(input("digite um angulo: "))
rad = math.radians(num)
sen = math.sin(rad)
coss = math.cos(rad)
tanj = math.tan(rad)
print(f"O seno é {sen:.2f}\no cosseno {coss:.2f}\ne atanjente é de {tanj:.2f}")

#sortear um nome
import random
n1 = str(input("digite um nome: "))
n2 = str(input("digite um nome: "))
n3 = str(input("digite um nome: "))
lista = [n1, n2, n3]
escolhido = random.choice(lista)
print(f"o aluno sorteado é {escolhido}")
"""

import random
#sortear ordem de uma lista
n1 = str(input("digite um nome: "))
n2 = str(input("digite um nome: "))
n3 = str(input("digite um nome: "))
lista = [n1, n2, n3]
escolha = random.shuffle(lista)
print(lista)
