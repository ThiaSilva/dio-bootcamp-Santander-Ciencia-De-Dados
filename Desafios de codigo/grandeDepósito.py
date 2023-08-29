# Solicitar o valor do depósito
valor = float(input("Digite o valor do depósito: "))

if valor > 0:
    # Se o valor for maior que zero, significa um depósito válido
    # Atualizar o saldo da conta (neste exemplo, o saldo começa em zero)
    saldo_conta = 0
    saldo_conta += valor
    print(f"Depósito realizado com sucesso. Saldo atual: R$ {saldo_conta:.2f}")
elif valor == 0:
    # Se o valor for igual a zero, é considerado inválido
    print("Valor inválido. O valor do depósito deve ser maior que zero.")
else:
    # Se o valor for negativo, encerramos o programa
    print("Encerrando o programa.")
