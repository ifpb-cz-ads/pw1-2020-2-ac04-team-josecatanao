#6) Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.
n = int(input("Tabuada de: "))
inicio = int(input("digite o inicio da Tabuada :"))
fim = int(input("digite o fim da Tabuada :"))
x = inicio
while x <= fim:
	print(n ,'*', x,'=',n*x)
	x = x + 1