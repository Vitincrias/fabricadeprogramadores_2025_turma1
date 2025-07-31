def bradesco():
    saldo=int(input("Digite o saldo bancário: "))
    saque=int(input("Digite o valor de saque: "))

    if  saldo >= saque:
        saldo -= saque
        print("Você realizou um saque com sucesso. ")  
        print(saldo)
    else:
        print("Você não possui saldo suficiente para realizar essa operação. ")
        print(saldo)
#bradesco()

def depósito():
    dinheiro=int(input("Digite o valor do seu saldo: "))
    pix=int(input("Digite o valor do depósito: "))

    if  pix >= dinheiro:
        pix += dinheiro
        print("Você realizou um saque com sucesso. ")  
        print(pix)
    else:
        print("Você não possui saldo suficiente para realizar essa operação. ")
        print(pix)
#depósito()

def matematica():
    valor_parte = float(input("Insira o valor: "))
    porcentagem = float (input("Insira  o valor da porcentagem: "))
    
    if porcentagem <= 0:
        print("Outro valor menor que zero")
    else: 
        valor_total = valor_parte * (porcentagem/100)
        print(valor_total)
matematica()
