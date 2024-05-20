import textwrap

def menu():
    menu =  """
    ========== Seja bem vindo ao BANCO Ravena ==========
                 Selecione a opção desejada:
                 [D] Depositar
                 [S] Sacar
                 [E] Extrato
                 [NC] Nova Conta
                 [LC] Lista de contas
                 [NU] Novo Usuario
                 [Q] Sair
                
            """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
                #print(saldo)
                saldo += valor
                extrato += f"Deposito de + R$ {valor:.2f}\n"
                print(f"Seu saldo atual é de: {saldo:.2f}")
                valor = 0
    else:
                print("Operação invalida !!!")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite
        
    excedeu_saque = saques_diarios > limite_saques

    if excedeu_limite:
        print(f"Valor informado maior que o limite para saque de sua conta, seu limite por saque é de {limite:.2f}\n")
        
    elif excedeu_saldo:
        print(f"Seu saldo é de {saldo:.2f}, insuficiente para a operação! \n")
        
    elif excedeu_saque: 
        print(f"Seu limite maximo de saques ao dia é de {limite_saques}, o mesmo ja foi excedido")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque de - R$ {valor:.2f}\n"
        saques_diarios += 1
        print(f"Seu saldo atual é de: {saldo:.2f}")
        valor = 0
    else:
        print("Operação invalida !!!")           

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Sem historico de movimentações." if not extrato else extrato)
    print(f"\nSaldo Atual: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("### Usuario ja Existe ###")
        return
    
    nome = input("Informe o nome e sobrenome: ")
    data_nascimento = input("Informe a data de nascimento (dia/mes/ano): ")
    endereco = input("Informe o endereço (Logradouro, NR - Bairro - Cidade/Estado[XX]): ")

    usuarios.append({"nome": nome, "data_nasciemnto": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuario criado com Sucesso !")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    saques_diarios = 0
    usuarios = []
    contas = []
   
    while True:
        opcao = menu()
        
        if opcao == "d":
            valor = float(input("Informe o valor do Deposito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "s":
            valor = float(input("Informe o valor do Saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=saques_diarios,
                limite_saques=LIMITE_SAQUES,
            )
    
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "q":
            break
    
        else:
            print("Seleção indisponiel, por favor selecione uma opção valiada")

main()