#8) Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.

n1 = int(input("Digite um número:"))
n2 = int(input("Digite um número:"))

nu1=n1
nu2=n2
cont = 0
para = 0

while para != 1 :  
  if n1<n2 or n1%n2==1 :
    para = 1
  else:
    n1=n1-n2
    cont +=1

print("********")
print(nu1," ÷ ",nu2," = ",cont)
print("********")
 