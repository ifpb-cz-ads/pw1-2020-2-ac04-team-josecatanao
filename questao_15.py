import os
#15) Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida. Repita até que a opção "saída" seja escolhida.
sair = 0

while sair != 999:
  print("******************")
  print("Digite '1' Para: Adição")
  print("Digite '2' Para: Subtração")
  print("Digite '3' Para: Divisão")
  print("Digite '4' Para: Multiplicação")
  print("Digite '5' Para: Sair")
  print("******************")
  escolha = input("Digite a sua escolha :")
  print("******************")
  if escolha == "1":
        for count in range(10):
           count+=1
           print(1,"+",count,"=",count+1)
  elif escolha == "2":
       for count in range(10):
           count+=1
           print(1,"-",count,"=",count-1)
  elif escolha == "3":
       for count in range(10):
           count+=1
           print(1,"/",count,"=",count/1)
  elif escolha == "4":
       for count in range(10):
           count+=1
           print(1,"*",count,"=",count*1)
  elif escolha == "5":  
      sair = 999  
  else:
    os.system('clear')
    print("Código inválido.")
  

