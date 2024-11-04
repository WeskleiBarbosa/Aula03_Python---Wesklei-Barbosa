idades = []
n = int(input("Quantas pessoas tem na turma? "))

for i in range(n):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    idades.append(idade)

media = sum(idades) / n

if 0 <= media <= 25:
    print("Turma Jovem")
elif 26 <= media <= 60:
    print("Turma Adulta")
else:
    print("Turma Idosa")
