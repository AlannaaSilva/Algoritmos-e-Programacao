"""
Beecrowd | 1179
Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares ou ímpares. Só que o tamanho de cada um dos dois vetores é de 5 posições. Então, cada vez que um dos dois vetores encher, você deverá imprimir todo o vetor e utilizá-lo novamente para os próximos números que forem lidos. Terminada a leitura, deve-se imprimir o conteúdo que restou em cada um dos dois vetores, imprimindo primeiro os valores do vetor impar. Cada vetor pode ser preenchido tantas vezes quantas for necessário.

Entrada
A entrada contém 15 números inteiros.

Saída
Imprima a saída conforme o exemplo abaixo.

"""

par = []
impar = []

for i in range (0,15):
  x= int(input())
  if x%2==0:
    par.append(x)
  if x%2!=0:
    impar.append(x)
  if len(par) == 5:
    for i in range(0,5):
      print (f"par[{i}] = {par[i]}")
    par = []
  if len(impar) == 5:
    for i in range(0,5):
      print (f"impar[{i}] = {impar[i]}")
    impar = []
for i in range (0,len(impar)):
  print (f"impar[{i}] = {impar[i]}")
for i in range (0,len(par)):
  print (f"par[{i}] = {par[i]}") 