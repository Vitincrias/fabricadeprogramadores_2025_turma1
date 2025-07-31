def depósito(:
    dinheiro=int(input("Digite o saldo"))
    pix=int(input("Digite o valor do depósito"))

    if  pix >= dinheiro:
        pix = pix + dinheiro
        print("Você realizou um saque com sucesso. ")  
        print(pix)
    else:
        print("Você não possui saldo suficiente para realizar essa operação. ")
        print(pix)
depósito)