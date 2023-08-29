# Sistema de cobrana utilizando while para fazer a recorrencia da cobrança

nomeCliente = input("Qual nome do cliente deseja cobrar: ")
valorDevendo = float(input("Qual valor o cliente esta devendo: "))
contatos = dict (telefone="5555-5555",email="carvalhot@gmail.com",)


while valorDevendo > 0:
    print(f"Ligando para cliente {nomeCliente} telefone {contatos['telefone']}, e enviando email para {contatos['email']}...")
    pagamento = int(input("Valor que deseja pagar: "))
    print(f"Saldo devedor é de: {valorDevendo}")
    print(f"Valor pago é de {pagamento}:")
    print(f"Novo saldo devedor é de: {valorDevendo - pagamento}")
    

    if pagamento <= valorDevendo:
        valorDevendo -= pagamento
    else:
        print("O pagamento excede o saldo devedor. Digite um novo valor de pagamento.")

print("Saldo devedor quitado!")






