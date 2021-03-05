#18) Escreva um programa que calcule o resto da divisão inteira entre dois números. Utilize apenas as operações de soma e subtração para calcular o resultado.

n1 = int(input("Digite um número:"))
n2 = int(input("Digite um número:"))

nu1=n1
nu2=n2
cont = 0
para = 0
fim=0
resto = 0
while para != 1 :  
  if n1<n2 :
    para = 1
  else:
    n1=n1-n2
    cont +=1
    
while fim<cont:
   resto=resto+n2
   fim+=1

print("********")
print(nu1,"%",nu2,"=",nu1-resto)
print("********")

  
