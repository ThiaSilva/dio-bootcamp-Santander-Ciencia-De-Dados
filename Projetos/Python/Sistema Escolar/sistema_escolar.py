# Sistemas de notas para testar condiçoes 

# Entrada nome do Aluno
nome = input("Qual o nome do aluno que deseja: ")

# Entrada da idade
idade = int(input(f"Qual a idade do aluno {nome}: "))

# Constante com a nota de corte do aluno
MEDIA_DE_CORTE = 6

# Cadastro das notas obtidas no semestre
notaA1 = int(input("Digite a primeira nota: " ))
notaA2 = int(input("Digite a Segunda nota: " ))
notaProjeto = int(input("Digite a nota do projeto: " ))

# Media das notas obtida 
mediaFinal = notaA1 + notaA2 + notaProjeto // 3

print(f" A média do final do aluno {nome}, é: {mediaFinal}")

# Possiveis status de fechamento
situacao_1 = "Aprovado"
situacao_2 = "Reprovado"

# Condição para saber a situação do aluno 

if mediaFinal < MEDIA_DE_CORTE: 
    print(f"O Aluno {nome}, esta {situacao_2}")
elif mediaFinal >= MEDIA_DE_CORTE:
    print(f"O Aluno {nome}, esta {situacao_1}")
