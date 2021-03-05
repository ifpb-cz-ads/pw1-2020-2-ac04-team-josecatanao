import os
#14) Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de códigos abaixo para obter o preço de cada produto:

erro = 999
quantidade = 0
while erro !=0 :
  print("=========================================")
  cod = input('Digite o codigo do produto:')
  quant = int(input('Digite a quantidade do produto:'))
  print("=========================================")
  if cod == "1":
     quantidade += quant*0.50
  elif cod == "2":
     quantidade += quant*1.00
  elif cod == "3":
     quantidade += quant*4.00
  elif cod == "5":
     quantidade += quant*7.00
  elif cod == "9":  
     quantidade += quant*8.00
  elif cod == "0":
     print("*************************************")
     print("O valor à pagar: ",quantidade)
     print("*************************************")
  else:
    os.system('clear')
    print("Código inválido.")
    

      