'''
Dados os nomes e notas de cada aluno em uma classe de N alunos, armazene-os em uma lista aninhada e imprima o(s) nome(s) de qualquer aluno(s) com a segunda nota mais baixa.

Nota: Se houver vários alunos com a segunda nota mais baixa, ordene seus nomes em ordem alfabética e imprima cada nome em uma nova linha.
'''

students = []
scorelist = []
for _ in range(int(input())):
  name = input()
  score = float(input())
  students.append([name, score])
  scorelist.append(score)
print(students)
sorted_scores = sorted(list(set(scorelist)))[1]
print(sorted_scores)
for i, j in sorted(students):
  if j == sorted_scores:
    print(i)