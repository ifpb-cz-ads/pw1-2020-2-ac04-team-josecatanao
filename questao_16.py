#16) Escreva um programa que leia um número e verifique se é ou não um número primo. Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número lido. Se o resto de uma dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.

num = int(input("Digite um número: "))
contador = 0

for i in range(1, num + 1):
    if num % i == 0:
        contador += 1
if contador == 2:
    print("O número é primo")
else:
    print("O número não é primo")