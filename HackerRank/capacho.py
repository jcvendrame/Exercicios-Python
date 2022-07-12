'''
O Sr. Vincent trabalha em uma empresa de fabricação de capachos. Um dia, ele projetou um novo capacho com as seguintes especificações:

* O tamanho do tapete deve serX. (é um número natural ímpar, eévezes.)
* O design deve ter 'BEM-VINDO' escrito no centro.
* O padrão de design deve usar apenas caracteres |e ..-

Projeto de Amostra (9X27)
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
'''
n, m = map(int, input().split())
for i in range(1, n, 2):
  print(str('.|.' * i).center(m, '-'))
print('Welcome'.center(m, "-"))
for i in range(n-2, -1, -2):
  print(str('.|.' * i).center(m, '-'))