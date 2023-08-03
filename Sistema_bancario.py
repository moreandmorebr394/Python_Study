menu = """

[d] Depositar
[s] Saldo
[e] Extrato
[q] Sair 

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opçao = input(menu)

    if opçao == "d":
        valor = float (input("Informe o valor a ser depositado:"))

        if valor > 0:
            print (f"Deposito realizado com sucesso R$ R$ {valor:.2f}\n")
            saldo += valor
            extrato += f'Depósito realizado: {valor:.2f}\n"

        else:
            print("Operação falhou: O valor informado é inválido")

    elif opçao == "s":

        valor = float(input("Informe o valor de saque:"))

        excedeu_saldo = valor > limite
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limites_saques

        if excedeu_saldo:
            print("Operação falhou, Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou, O valor do saque excede o limite")

        elif excedeu_saques:
            print("Operação falou, O número máximo de saque atingido.")

        elif valor > 0:
            print(f "Saque realizado com sucesso. {valor:.2f}\n")
            saldo -= valor
            extrato += f"Saque realizado : {valor:.2f}\n"

        else:
            print("Operação falhou: O valor informado é inválido")

        
    elif opçao == "e"
        print("Extrato")
        print("Não foram realizado movimentações na conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opçao == "q":
        break

    else: 
        print("Operção inválida, por favor selecione um comando válido.")
