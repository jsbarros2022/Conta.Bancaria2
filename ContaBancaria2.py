import textwrap

def menu():
    menu = """
    ============MENU=============
    [d]\tDepositar
    [d]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\t Listar Contas
    [nu]\Novo Usuário
    [q]\tSair
    =>"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato,/):
    if valor >0:
            saldo += valor
            extrato+= f"Deposito: R${valor:.2f}\n"
    else:
            print("\n== Operação falhou! O valor informado é inválido")
    return saldo, extrato


def sacar (*,saldo, valor, extrato, limite, numero_saques, limite_saques):
        excedeu_saldo = valor> saldo
        excedeu_limite = valor>limite
        execedeu_saque = numero_saques>limite_saques
        if excedeu_saldo:
             print("\n@@ Operação falhou! Saldo insuficiente")
        elif excedeu_limite:
             print("\n@@ Operação falhou! Você excedeu limite")
        elif execedeu_saque:
             print("\n@@ Operação falhou! Você excedeu limite de saques diario")
        elif valor > 0:
            saldo-=valor
            extrato+= f"Saque: R${valor:.2f}\n"
            numero_saques+=1
            print("\n==Saque realizado com sucesso")
        else:
              print("\n@@ Operação falhou! Valor informado é inválido")
        return saldo, extrato
  
          

def exibir_extrato(saldo, /,*, extrato):
     print("\n ====================EXTRATO==================")
     print("Não forma realizadas treansações " if not extrato else extrato)
     print(f"\nSaldo: R$ {saldo:.2f}")
     print("==================================================")
     


def criar_usuario(usuarios):
     cpf = input("Informa seu CPF(somente numeros):")
     usuario = filtrar_usuario(cpf,usuarios)
     if usuario:
          print("\n@@@ Já existe usuario com este CPF! @@@")
          return
     nome = input("Informe o nome completo:")
     data_nascimento = input("Informe a data de nascimento(dd-mm-aaa):" )
     endereco = input("Informe o endereço(logradouro,nro-bairro-cidade/sigla estado):")

     usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf": cpf, "endereco":endereco})
     print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuario):
     usuarios_filtrados = [usuario for usuarios in usuario if usuario ["cpf" == cpf]]
     return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuario):
     cpf = input("Digite o CPF do usuario:")
     usuario.filtrar_usuario(cpf,usuario)

     if usuario:
          print("\n Conta criada com sucesso")
          return {"agencia": agencia, "numero_conta": numero_conta,"usuario": usuario }
     print("\n@@@ Usuário não encontrato, fluxo de criação de conta encerrado!@@@")
     return  None

def listar_contas(contas):
     


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite  = 500
    extrato = ""
    numero_saques = 0
    usuarios= []
    contas = []

    while True: 
        opcao = input(menu)
        if opcao == "d":
            valor = float(input("Informe o valor do deposito:"))
            saldo, extrato=depositar(saldo,valor,extrato)
           
        elif opcao == "s":
            valor = float(input("Informe o valor do saque:"))
            saldo,extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
            
        elif opcao == "nc":
            numero_conta = len(contas)+1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
             contas.append(conta)
        
        elif opcao == "lc":
             listar_contas(contas)
            
        elif opcao == "q":
             break
        else:
             print("Operação inválida, por favor selecione a operação desejada")          



main()