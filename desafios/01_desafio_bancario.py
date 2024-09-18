menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_DE_SAQUES = 3
depositos = []
saques = []

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_depositado = float(input("Digite qual o valor deseja depositar: "))

        if valor_depositado > 0:
            saldo += valor_depositado
            depositos.append(valor_depositado)
            extrato += str(valor_depositado)
            print(f"Depósito: R$ {valor_depositado:.2f} realizado com sucesso!\n")
        else:
            print("Operação Falhou! Valor inserido não é válido")

    elif opcao == "s":
            valor_sacado = float(input("Digite qual o valor deseja sacar: "))

            if valor_sacado > 0 and numeros_saques < LIMITE_DE_SAQUES and valor_sacado <= limite and saldo >= valor_sacado:
                saldo -= valor_sacado
                numeros_saques += 1
                saques.append(valor_sacado)
                extrato += str(valor_sacado)
                print(f"Saque de R$ {valor_sacado:.2f} realizado com sucesso!")
                
            elif(valor_sacado < 0):
                print("Operação Falhou! Valor inserido não é válido")

            elif(numeros_saques >= 3):
                print("Operação Falhou! É permitido somente 3 saques diários.")

            elif(valor_sacado > limite):
                print("Operação Falhou! É permitido somente até R$ 500.00 por saque")

            elif(saldo < valor_sacado):
                print("Operação Falhou! Saldo Insuficiente.")

    elif opcao == "e":
        print("----------EXTRATO----------")

        if not extrato:
            print("Nao foram realizadas movimentações.")

        print("Depositos realizados:")
        for deposito in depositos:
            print("R$ "+f"{deposito:.2f}")
        
        print("\nSaques realizados:")
        for saque in saques:
            print("R$ "+f"{saque:.2f}")

        print(f"\n\nSaldo Atual: R$ {saldo:.2f}")
        print("---------------------------")

    elif opcao == "q":
        break

    else:
        print("Operação Inválida, por favor selecione novamante a operação desejada.")