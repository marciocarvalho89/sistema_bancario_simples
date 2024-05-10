menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Qual valor?"))
        if deposito>0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        else:
            print("Valor inválido")
        
    elif opcao == "s":
        while(numero_saques < LIMITE_SAQUES):
            saque = float(input("Qual o valor para saque?"))
            if saque > saldo or saque > 500:
                print("Saque não pôde ser realizado")
            else:
                saldo -= saque
                numero_saques += 1
                extrato += f"Saque: R$ {saque:.2f}\n"

    elif opcao == "e":
        if extrato != "":
            print(extrato)
            print(f"O saldo atual é: R$ {saldo:.2f}")
        else:
            print("Não foram realizadas movimentações")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")