# Enunciado: Crie um programa que receba a nota de 5 alunos e exiba quantos foram aprovados (nota maior ou igual a 7).
aprovados = 0

for nt in range(5):
    nota = float(input("Digite a nota do aluno :"))

    if nota >= 7:
        aprovados += 1

        print(f'total de alunos aprovados: {aprovados}')
        