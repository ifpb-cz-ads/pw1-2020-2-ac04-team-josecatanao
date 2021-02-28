#13) Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

cont = 0
n = 1
soma = 0
media = 0

listaN = []
while n != 0 :
    n = int(input("Digite um numero :"))
    if n == 0:
      break
    cont +=1  
    listaN.append(n)

soma = sum(listaN)
media = soma/cont
print('Total de Números Digitados: ',cont)
print('A soma total: ',soma)
print('Média Aritmética: ',media)

