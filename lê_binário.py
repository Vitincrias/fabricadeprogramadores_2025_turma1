def lê_binário():
    try:
        with open("10" ,"rb") as fs1:
            dados=fs1.read()
            print(type(dados))
        with open("10" ,"wb") as fs2:
            fs2.write(dados)
        with open("10" ,"rb") as fs3:
            fs3.write(dados)
    except FileNotFoundError as e:
        print('Arquivo não existe! -_-|||', e)
    except IOError as e:
        print('Deu algo errado @_@') 
    print("OK! ~_~")
lê_binário()

