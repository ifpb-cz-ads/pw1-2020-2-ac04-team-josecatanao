#17) Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.

num= int(input('Digite um número :'))
contatador = 0
n = 2
while contatador < num:
    primo = True
    for i in range(2, n):
        if n % i == 0:
           primo = False
           break
    if primo:
        print(n)
        contatador += 1
    n += 1
