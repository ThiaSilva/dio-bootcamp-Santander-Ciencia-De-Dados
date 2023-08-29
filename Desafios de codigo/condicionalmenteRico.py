# Entrada de dados
saldo_total = int(input())
valor_saque = int(input())

# TODO: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.

saldo = saldo_total - valor_saque

if valor_saque <= saldo_total and saldo > 100:
  print(f"Saque realizado com sucesso. Novo saldo: {saldo}")
elif valor_saque <= saldo_total and saldo <= 100:
  print(f"Saque realizado com sucesso. Novo saldo: {saldo}")
else:
  print("Saldo insuficiente. Saque nao realizado!")