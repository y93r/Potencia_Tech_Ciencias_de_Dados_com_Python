menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[f] Finalizar
'''

saldo = 0
limite = 500
extrato = ''
numero_saque = 0
limite_saque = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        try:
            valor = float(input('Informe o valor do depósito: '))
            if valor <= 0:
                raise ValueError('O valor informado não é válido!')

            saldo += valor
            extrato += f'Depósito: R${valor:.2f}\n'

        except ValueError as e:
            print('Erro:', str(e))

    elif opcao == 's':
        try:
            valor = float(input('Informe o valor de saque: '))

            excedeu_condicoes = valor > saldo or valor > limite or numero_saque >= limite_saque

            if excedeu_condicoes:
                if valor > saldo:
                    print('Erro! Você não tem saldo suficiente!')
                elif valor > limite:
                    print('Erro! O valor do saque excede o limite')
                elif numero_saque >= limite_saque:
                    print('Erro! Número máximo de saques excedidos')
            elif valor <= 0:
                print('Erro! O valor informado é inválido')
            else:
                saldo -= valor
                extrato += f'Saque: {valor:.2f}\n'
                numero_saque += 1

        except ValueError:
            print('Erro! Digite um número válido.')

    elif opcao == 'e':
        print('\n=========== EXTRATO ===========')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R${saldo:.2f}')
        print('=================================')

    elif opcao == 'f':
        print('Processo finalizado')
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada')
