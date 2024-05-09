menu = """
========== Seja bem vindo ao BANCO Ravena ==========
             Selecione a opção desejada:
             [D] Depositar
             [S] Sacar
             [E] Extrato
             [Q] Sair
"""

depositar = 0
saldo = float(00.00)
extrato = ""
limite = 500
saques_diarios = 0
LIMITE_SAQUE = 3

while True:
    
    opcao = input(menu)
        
    if opcao == "d":
        valor = float(input("Informe o valor do Deposito: "))
            
        if valor > 0:
            #print(saldo)
            saldo += valor
            extrato += f"Deposito de + R$ {valor:.2f}\n"
            print(f"Seu saldo atual é de: {saldo:.2f}")
            valor = 0

        else:
            print("Operação invalida !!!")
    elif opcao == "s":
        valor = float(input("Informe o valor do Saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite
        
        excedeu_saque = saques_diarios > LIMITE_SAQUE

        if excedeu_limite:
            print(f"Valor informado maior que o limite para saque de sua conta, seu limite por saque é de {limite:.2f}\n")
        
        elif excedeu_saldo:
            print(f"Seu saldo é de {saldo:.2f}, insuficiente para a operação! \n")
        
        elif excedeu_saque: 
            print(f"Seu limite maximo de saques ao dia é de {LIMITE_SAQUE}, o mesmo ja foi excedido")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de - R$ {valor:.2f}\n"
            saques_diarios += 1
            print(f"Seu saldo atual é de: {saldo:.2f}")
            valor = 0
        else:
            print("Operação invalida !!!")
    
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Sem historico de movimentações." if not extrato else extrato)
        print(f"\nSaldo Atual: R$ {saldo:.2f}")
        print("==========================================")
    
    elif opcao == "q":
        break
    
    else:
        print("Seleção indisponiel, por favor selecione D - S - E Q, Deposito, Saque, Extrato ou Sair respequitivamente.")