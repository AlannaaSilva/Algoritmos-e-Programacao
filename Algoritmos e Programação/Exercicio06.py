"""
Beecrowd | 1176

A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 46).

Saída
Os valores devem ser mostrados na mesma linha, separados por um espaço em branco. Não deve haver espaço após o último valor.
"""

N = int(input()) 

anterior = 0 
posterior = 1 
i = 3

if N >= 2:
  print(anterior, posterior, end="")
  
while i <= N:
    soma = posterior + anterior
    print("", soma, end="")
    anterior = posterior
    posterior = soma
    i = i + 1
if N == 1:
 print( anterior, end="\n")

print (end="\n")