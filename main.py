nome = str(input('Digite seu nome: '))
print('*' * 30)
print(f"""       Seja Bem vindo
         Banco DIO!
      Sr(a) {nome} """)
print('*' * 30)
print()

limite_saque = 3
extrato = 0
numero_saques = 0
saldo = 0

while True:
    print("""Opções:
      [1] Extrato
      [2] Depositar
      [3] Sacar""")
    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        print(f'Você possui R${extrato} em conta.')
        print()
    
    elif opcao == 2:
        deposito = int(input('Valor do depósito R$: '))
        saldo += deposito
        print(f'Seu saldo é R${saldo} ')
        extrato = saldo

    elif opcao == 3:
        if numero_saques < limite_saque:
            saque = int(input('Valor do saque R$: '))
            if saque > 0:
                if saque <= 500:
                    if saldo >= saque:
                        saldo -= saque
                        print(f'Saque de R${saque} realizado com sucesso.')
                        extrato = saldo
                        numero_saques += 1
                    else:
                        print('Saldo insuficiente para o saque.')
                else:
                    print('Valor máximo de saque é R$500.')
            else:
                print('O valor do saque deve ser maior que zero.')
        else:
            print('Limite de saques atingido.')
        print()

    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')
        print()
