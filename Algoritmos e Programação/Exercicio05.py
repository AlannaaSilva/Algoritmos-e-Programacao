"""
Beecrowd | 3137
As páginas de um livro são numeradas de 1 até a última página P. Dada a quantidade de páginas de um livro, sua tarefa é informar quantos dígitos foram usados para numerar este livro, da página 1 até a página P.

Entrada
A entrada é formada por uma única linha contendo um inteiro P (que varia de 1 a menos de 1 milhão), que representa o número total de páginas do respectivo livro.

Saída
A saída é composta por uma única linha na saída, contendo a quantidade de dígitos que foram usados para numerar todas as P páginas do livro, da página 1 até a página P.
n=int(input())

"""
somatorio_9=9
somatorio_99=189
somatorio_999= 2889
somatorio_9999=38889
somatorio_99999=488889
somatorio_999999=5888889

x=0

if n>=1 and n<=9:
  print(n)
  
if n>=10 and n<=99:
  x= (n-9)*2
  x= x+(somatorio_9)
  print(x)
  
if n>=100 and n<=999:
  x=(n-99)*3
  x= x+somatorio_99
  print(x)
    
if n>=1000 and n<=9999:
  x= (n-999)*4
  x= x+somatorio_999
  print(x)
  
if n>=10000 and n<=99999:
  x= (n-9999)*5
  x= x+somatorio_9999
  print(x)
  
if n>=100000 and n<=999999:
  x= (n-99999)*6
  x= x+somatorio_99999
  print(x)