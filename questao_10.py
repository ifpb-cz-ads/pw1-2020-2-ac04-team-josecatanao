#10) Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 12 primeiros meses. Escreva o total ganho com juros no período.

valor = float(input("Inicial: "))
taxa = float(input("Taxa:"))
cont = 1
saldo = valor
while cont <= 12:
    saldo = saldo + (saldo * (taxa / 100))
    print(f"{cont}° Saldo: R${saldo:5.2f}.")
    cont = cont + 1
print(f"O valor obtido: R${saldo-valor:8.2f}.")