#7) Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

nu1=int(input('digite o primeiro número :'))
nu2=int(input('digite o segundo número :'))

cont=1
somador=0
while cont<=nu2 :
  somador = somador+nu1
  cont = cont + 1
print(nu1,'*',nu2,'=',somador)
