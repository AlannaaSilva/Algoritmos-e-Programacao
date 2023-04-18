""" 
Beecrowd | 3134
Sem ter muito o que fazer, você decidiu equilibrar quatro pacotes em uma balança. Para conseguir equilibrar,
você precisa colocar o mesmo peso no prato da esquerda que no prato da direita. Sua tarefa é, dados os pesos dos
quatro pacotes, informar se é possível colocar todos os quatro pacotes nos pratos de uma forma que a balança fique
equilibrada. Você pode tentar qualquer configuração dos quatro pacotes nos dois pratos para isso (não apenas dois pacotes em cada prato).

Entrada
A entrada é composta por quatro linhas, cada uma delas informando o peso de um dos quatro pacotes. O peso de um pacote é informado como um
número real com uma casa decimal, variando de 0.1 a 30.0.

Saída
A saída deve ser YES em uma linha isolada, caso haja alguma forma de organizar os quatro pacotes nos dois pratos da balança de tal forma que a balança fique equilibrada.
Se não houver uma forma da balança ficar equilibrada, a saída deve ser NO em uma linha isolada. 
"""

p1=float(input())
p2=float(input())
p3=float(input())
p4=float(input())

p1=p1*10
p2=p2*10
p3=p3*10
p4=p4*10

if p1+p2 == p3+p4 or p1+p3 == p2+p4 or p1+p4 == p2+p3 or p1 == p2+p3+p4 or p2 == p1+p3+p4 or p3 == p1+p2+p4 or p4 == p1+p2+p3:
  print("YES")
else:
  print("NO")