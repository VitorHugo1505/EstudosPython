"""
lucro = 1000 - 300

imposto é de 15% sobre o faturamento

lucro = 1000 - 300 - 0.15 * 1000
# isto esta errao pois não é eficiente
"""

# O correto seria
faturamento = 1000
custo = 300
imposto = 0.15

lucro = faturamento - custo - imposto * faturamento

print(lucro)

#tipos de variaveis
#int -> numeros inteiros
#float -> numeros com casa decimal
#string -> textos
#bool -> verdadeiros ou falso

