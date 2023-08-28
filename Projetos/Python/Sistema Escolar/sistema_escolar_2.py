### Segunda versão do projeto Sistemas escolar 
### Implementando condição de passagem por conselho com base em faltas e comportamento

NOTA_DE_CORTE = 6

nome = input("Nome do aluno: ")

nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))
nota3 = int(input("Nota 3: "))
nota4 = int(input("Nota 4: "))

mediaFinal = (nota1 + nota2 + nota3 + nota4) // 4

comportamento = input("O aluno possui bom comportamento: ")

if mediaFinal >= NOTA_DE_CORTE: 
    print(f"O Aluno esta aprovado: com nota {mediaFinal}" )
elif mediaFinal < NOTA_DE_CORTE and comportamento == "sim" :
    print(mediaFinal)
    print(f"O Aluno esta aprovado por conselho com nota {mediaFinal} por bom comportamento")
else:
    print(mediaFinal)
    print("Aluno Reprovado")
