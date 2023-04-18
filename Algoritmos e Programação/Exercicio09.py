
# Faça um programa que pede para o usuário informar 4 números reais, todos diferentes entre si. Imprima esses quatro números reais em ordem crescente. 

n1 = input()
n2 = input()
n3 = input()
n4 = input()

primeiro_numero = 0
segundo_numero = 0
terceiro_numero = 0
quarto_numero = 0

if n1 >= n2 and n1 >= n3 and n1 >= n4:
  quarto_numero = n1
  if n2 >= n3 and n2 >= n4:
      terceiro_numero = n2
      if n3 >= n4:
        segundo_numero = n3
        primeiro_numero = n4
      else:
        segundo_numero = n4
        primeiro_numero = n3
  if n3 >= n2 and n3 >= n4:
      terceiro_numero = n3
      if n2 >= n4:
        segundo_numero = n2
        primeiro_numero = n4
      else:
        segundo_numero = n4
        primeiro_numero = n2
  if n4 >= n2 and n4 >= n3:
      terceiro = n4
      if n2 >= n3:
        segundo_numero = n2
        primeiro_numero = n3
      else:
        segundo_numero = n3
        primeiro_numero = n2

# AGORA EU VOU TESTAR COM n2 SENDO O MAIOR : 

if n2 >= n1 and n2 >= n3 and n2 >= n4:
  quarto_numero = n2
  if n1 >= n3 and n1 >= n4:
      terceiro_numero = n1
      if n3 >= n4:
        segundo_numero = n3
        primeiro_numero = n4
      else:
        segundo_numero = n4
        primeiro_numero = n3
  if n3 >= n1 and n3 >= n4:
      terceiro_numero = n3
      if n1 >= n4:
        segundo_numero = n1
        primeiro_numero = n4
      else:
        segundo_numero = n4
        primeiro_numero = n1
  if n4 >= n1 and n4 >= n3:
      terceiro_numero = n4
      if n1 >= n3:
        segundo_numero = n1
        primeiro_numero = n3
      else:
        segundo_numero = n3
        primeiro_numero = n1

# AGORA EU VOU TESTAR COM n3 SENDO O MAIOR : 

if n3 >= n1 and n3 >= n2 and n3 >= n4:
  quarto_numero = n3
  if n2 >= n1 and n2 >= n4:
      terceiro_numero = n2
      if n1 >= n4:
        segundo_numero = n1
        primeiro_numero = n4
      else:
        segundo_numero = n4
        primeiro_numero = n1
  if n1 >= n2 and n1 >= n4:
      terceiro_numero = n1
      if n2 >= n4:
        segundo_numero = n2
        primeiro_numero = n4
      else:
        segundo_numero = n4
        primeiro_numero = n2
  if n4 >= n2 and n4 >= n1:
      terceiro_numero = n4
      if n2 >= n1:
        segundo_numero = n2
        primeiro_numero = n1
      else:
        segundo_numero = n1
        primeiro_numero = n2

        
# AGORA EU VOU TESTAR COM n4 SENDO O MAIOR : 

if n4 >= n1 and n4 >= n2 and n4>= n3:
  quarto_numero = n4
  if n2 >= n1 and n2 >= n3:
      terceiro_numero = n2
      if n1 >= n3:
        segundo_numero = n1
        primeiro_numero = n3
      else:
        segundo_numero = n3
        primeiro_numero = n1
  if n3 >= n2 and n3 >= n1:
      terceiro_numero = n3
      if n2 >= n1:
        segundo_numero = n2
        primeiro_numero = n1
      else:
        segundo_numero = n1
        primeiro_numero = n2
  if n1 >= n2 and n1 >= n3:
      terceiro_numero = n1
      if n2 >= n3:
        segundo_numero = n2
        primeiro_numero = n3
      else:
        segundo_numero = n3
        primeiro_numero = n2
        
print(primeiro_numero)
print(segundo_numero)
print(terceiro_numero)
print(quarto_numero)