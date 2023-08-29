# Entrada de dados
valor_inicial = float(input("Digite o valor inicial do investimento: "))
taxa_juros = float(input("Digite a taxa de juros anual (em decimal): "))
periodo = int(input("Digite o período em anos: "))

# Função para calcular o valor final do investimento com juros compostos
def calcular_valor_final(valor_inicial, taxa_juros, periodo):
    valor_final = valor_inicial * (1 + taxa_juros) ** periodo
    return valor_final



# Chama a função para calcular o valor final
valor_final = calcular_valor_final(valor_inicial, taxa_juros, periodo)

# Imprime o valor final do investimento
print(f"Valor final do investimento: R$ {valor_final:.2f}")