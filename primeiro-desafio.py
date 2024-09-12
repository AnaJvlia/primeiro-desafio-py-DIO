# Criar sistema bancário com as operações: sacar, depositar e visualizar extrato

menu = -1
saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while menu != 0:
    menu = int(input ("Informe uma opção:\n[1] Depositar \n[2] Sacar \n[3] Extrato \n[0] Sair\n"))

# Depósito: devem ser armazenados em uma variável e exibidos na operação de extrato, não deve ser possível depositar valores negativos 
    if menu == 1: 
        deposito = float(input("Qual valor deseja depositar? \n"))

        if deposito > 0: 
            saldo += deposito
            extrato += f"Depósito: R${deposito:.2f}\n"
            print("\n")
        
        else: 
            print("Por favor deposite um valor positivo!")

# Saque: limite de 3 saques diários no valor máximo de 500 reais por saque. Informar falta de saldo caso não tenha saldo em conta. Saques devem ser armazenados em uma variável e exibidos na operação de extrato
    elif menu == 2: 
        saque = float(input("Qual valor deseja sacar? \n"))

        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente para realizar o saque.")
            print("\n")
        
        elif excedeu_limite:
            print(f"Limite de valor por saque é R${limite}")
            print("\n")
        
        elif excedeu_saques:
            print(f"Você atingiu seu limite de {LIMITE_DE_SAQUES} saques diários")
            print("\n")
        
        elif saque > 0: 
            saldo -= saque 
            numero_de_saques += 1
            extrato += f"Saque: R${saque:.2f}\n"
            print(f"Valor sacado com sucesso! \nSaldo atual: R${saldo}")
            print("\n")
        
        else: 
            print("O valor informado é inválido.")

# Extrato: listar todos os depósitos e saques realizados na conta e no final exibir o saldo atual da conta
    elif menu == 3:
            print("------ EXTRATO ------")
            print("Ainda não foram realizadas movimentações na conta." if not extrato else extrato) #Verifica se o extrato está vazio. if not inverte valor de uma condição  
            print(f"Saldo atual: R${saldo}")
            print("---------------------")
            print("\n")       

# Sair
    elif menu == 0:
        break 

    else: 
        print("Digite uma opção válida")

             


